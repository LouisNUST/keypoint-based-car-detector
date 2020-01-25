"""Preprocess annotations with KITTI ground-truth"""

import os
import glob
import copy
import logging
from collections import defaultdict
import json
import datetime

from .transforms import transform_keypoints
from ..utils import get_calibration, split_training, parse_ground_truth, get_iou_matches, append_cluster
from ..network.process import preprocess_pifpaf, preprocess_monoloco

##! OPENPIFPAF REALTIME_PRED 
import openpifpaf
import torch
import PIL
import numpy as np

class PreprocessKitti:
    """Prepare arrays with same format as nuScenes preprocessing but using ground truth txt files"""

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    dic_jo = {'train': dict(X=[], Y=[], names=[], kps=[], boxes_3d=[], K=[],
                            clst=defaultdict(lambda: defaultdict(list))),
              'val': dict(X=[], Y=[], names=[], kps=[], boxes_3d=[], K=[],
                          clst=defaultdict(lambda: defaultdict(list))),
              'test': dict(X=[], Y=[], names=[], kps=[], boxes_3d=[], K=[],
                           clst=defaultdict(lambda: defaultdict(list)))}
    dic_names = defaultdict(lambda: defaultdict(list))

    def bbox_from_keypoints(self, kps):
        m = kps[:, 2] > 0
        if not np.any(m) or np.sum(m)<3:
            return [0, 0, 0, 0]

        x, y = np.min(kps[:, 0][m]), np.min(kps[:, 1][m])
        w, h = np.max(kps[:, 0][m]) - x, np.max(kps[:, 1][m]) - y
        return [x, y, w, h]


    def __init__(self, dir_ann, iou_min):

        self.dir_ann = dir_ann
        self.iou_min = iou_min
        self.dir_gt = os.path.join('data', 'kitti', 'gt')
        self.names_gt = tuple(os.listdir(self.dir_gt))
        self.dir_kk = os.path.join('data', 'kitti', 'calib')
        self.list_gt = glob.glob(self.dir_gt + '/*.txt')
        assert os.path.exists(self.dir_gt), "Ground truth dir does not exist"
        assert os.path.exists(self.dir_ann), "Annotation dir does not exist"

        now = datetime.datetime.now()
        now_time = now.strftime("%Y%m%d-%H%M")[2:]
        #dir_out = os.path.join('data', 'arrays')
        dir_out = dir_ann+"/../out"
        self.path_joints = os.path.join(dir_out, 'joints-kitti-' + now_time + '.json')
        self.path_names = os.path.join(dir_out, 'names-kitti-' + now_time + '.json')
        path_train = os.path.join('splits', 'kitti_train.txt')
        path_val = os.path.join('splits', 'kitti_val.txt')
        self.set_train, self.set_val = split_training(self.names_gt, path_train, path_val)

    def run(self):
        """Save json files"""


        # INIT of openpifpaf
        net, _ = openpifpaf.network.factory(checkpoint='/home/bonnesoe/semester_project/openpifpaf/outputs/resnet101-pif-paf-skeleton-edge420-191228-163858-5131e6a6.pkl')
        net = net.cuda()
        decode = openpifpaf.decoder.factory_decode(net, seed_threshold=0.5)
        processor = openpifpaf.decoder.Processor(net, decode, instance_threshold=0.05,keypoint_threshold=0.1)


        cnt_gt = cnt_files = cnt_files_ped = cnt_fnf = 0
        dic_cnt = {'train': 0, 'val': 0, 'test': 0}

        for name in self.names_gt:
            path_gt = os.path.join(self.dir_gt, name)
            basename, _ = os.path.splitext(name)

            phase, flag = self._factory_phase(name)
            if flag:
                cnt_fnf += 1
                continue

            # Extract keypoints
            path_txt = os.path.join(self.dir_kk, basename + '.txt')
            p_left, _ = get_calibration(path_txt)
            kk = p_left[0]

            # Iterate over each line of the gt file and save box location and distances
            boxes_gt, boxes_3d, dds_gt = parse_ground_truth(path_gt, category='all')[:3]

            self.dic_names[basename + '.png']['boxes'] = copy.deepcopy(boxes_gt)
            self.dic_names[basename + '.png']['dds'] = copy.deepcopy(dds_gt)
            self.dic_names[basename + '.png']['K'] = copy.deepcopy(kk)
            cnt_gt += len(boxes_gt)
            cnt_files += 1
            cnt_files_ped += min(len(boxes_gt), 1)  # if no boxes 0 else 1


            path_pif = os.path.join(self.dir_ann, basename + '.png.pifpaf.json')
            exists = os.path.isfile(path_pif)

            keypoints = None
            if exists:
                with open(path_pif, 'r') as file:
                    annotations = json.load(file)
                    boxes, keypoints = preprocess_pifpaf(annotations, im_size=(1238, 374))
                    
            else:
                pil_img = PIL.Image.open(os.path.join('data', 'kitti', 'images', basename +'.png'))
                data = openpifpaf.datasets.PilImageList([pil_img])
                loader = torch.utils.data.DataLoader(data, batch_size=1, pin_memory=True)
                #im = np.asarray(pil_img)

                for images_batch, _, __ in loader:
                    images_batch = images_batch.cuda()
                    fields_batch = processor.fields(images_batch)
                    predictions = processor.annotations(fields_batch[0])
                
                annotations = [ {
                            'keypoints': np.around(ann.data, 1).reshape(-1).tolist(),
                            'bbox': np.around(self.bbox_from_keypoints(ann.data), 1).tolist(),
                            'score': round(ann.score(), 3),
                        }
                        for ann in predictions
                        ]
                boxes, keypoints = preprocess_pifpaf(annotations, im_size=(1238, 374))
                #TODO 

            # Match each set of keypoint with a ground truth
            if keypoints:

                inputs = preprocess_monoloco(keypoints, kk).tolist()
                matches = get_iou_matches(boxes, boxes_gt, self.iou_min)
                for (idx, idx_gt) in matches:
                    self.dic_jo[phase]['kps'].append(keypoints[idx])
                    self.dic_jo[phase]['X'].append(inputs[idx])
                    self.dic_jo[phase]['Y'].append([dds_gt[idx_gt]])  # Trick to make it (nn,1)
                    self.dic_jo[phase]['boxes_3d'].append(boxes_3d[idx_gt])
                    self.dic_jo[phase]['K'].append(kk)
                    self.dic_jo[phase]['names'].append(name)  # One image name for each annotation
                    append_cluster(self.dic_jo, phase, inputs[idx], dds_gt[idx_gt], keypoints[idx])
                    dic_cnt[phase] += 1

        with open(self.path_joints, 'w') as file:
            json.dump(self.dic_jo, file)
        with open(os.path.join(self.path_names), 'w') as file:
            json.dump(self.dic_names, file)
        for phase in ['train', 'val', 'test']:
            print("Saved {} annotations for phase {}"
                  .format(dic_cnt[phase], phase))
        print("Number of GT files: {}. Files with at least one pedestrian: {}.  Files not found: {}"
              .format(cnt_files, cnt_files_ped, cnt_fnf))
        print("Matched : {:.1f} % of the ground truth instances"
              .format(100 * (dic_cnt['train'] + dic_cnt['val']) / cnt_gt))
        print("\nOutput files:\n{}\n{}\n".format(self.path_names, self.path_joints))

    def _factory_phase(self, name):
        """Choose the phase"""

        phase = None
        flag = False
        if name in self.set_train:
            phase = 'train'
        elif name in self.set_val:
            phase = 'val'
        else:
            flag = True
        return phase, flag
