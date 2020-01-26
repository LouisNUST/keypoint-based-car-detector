# Convert Bounding boxes in nuscenes to be trained with Monoloco

Function to convert the bounding box of the nuscenes dataset into a set of 9 keypoints to be trained and evaluated with Monoloco.

![Carfusion with bounding box](../docs/Carfusion_bbox.png)

# Installation

To make this notebook work, install the required packeges with :

pip install -r requirements.txt

# Necessary Modifications

The path of the nuscenes dataset needs to be given in the variable ```dir_nuscenes```.
To download nucenes, click [here](https://www.nuscenes.org/download) and extract the documents with the script ```functions/extract.sh``` provided.

# Visualize Monoloco with Bounding boxes.

**IMPORTANT**

A pretrained version of Monoloco on the preprocessed is already present in this folder and called ```hyp-monoloco-boxe.pkl```. The results of this trained version can be observed with the notebook visualization.ipynb.

To use it, change the dataset type [nuscenes or nuscenes-teaser] and change the path to the nuscenes dataset.