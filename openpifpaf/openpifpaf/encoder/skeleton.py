import numpy as np
import torch

from .annrescaler import AnnRescaler
from ..data import COCO_KEYPOINTS


class Skeleton(object):
    def __init__(self, *, max_instances=100, n_keypoints=len(COCO_KEYPOINTS)):
        self.max_instances = max_instances
        self.n_keypoints = n_keypoints

    def __call__(self, anns, width_height_original, v_th=0):
        rescaler = AnnRescaler(1, self.n_keypoints)
        keypoint_sets, __, ___ = rescaler(anns, width_height_original)

        out = np.zeros((self.max_instances, self.n_keypoints, 3), dtype=np.float32)
        for i, keypoints in enumerate(keypoint_sets):
            for f, xyv in enumerate(keypoints):
                if xyv[2] <= v_th:
                    continue
                out[i, f] = xyv

        return (torch.from_numpy(out),)
