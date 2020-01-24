from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
import os
pylab.rcParams['figure.figsize'] = (8.0, 10.0)

dataDir=os.curdir+"/datasets/carfusion"
dataType='keypoints_train'


# initialize COCO api for person keypoints annotations
#annFile = '{}/annotations/person_keypoints_{}.json'.format(dataDir,dataType)
annFile = '{}/annotations/car_{}.json'.format(dataDir,dataType)
coco_kps=COCO(annFile)

catIds = coco_kps.getCatIds(catNms=['car']);
imgIds = coco_kps.getImgIds(catIds=catIds );
myID = np.random.randint(0,len(imgIds));
print(myID)
img = coco_kps.loadImgs(imgIds[myID])[0]

print(coco_kps.getCatIds(),img)
I = io.imread(dataDir+"/train/"+img['file_name'])


# load and display keypoints annotations
plt.imshow(I); plt.axis('off')
ax = plt.gca()
annIds = coco_kps.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
anns = coco_kps.loadAnns(annIds)
coco_kps.showAnns(anns)
plt.show()

