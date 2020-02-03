# Carfusion Downloading and processing

![Carfusion with bounding box](../docs/Carfusion_bbox.png)

This part of the code is dedicated to the download and processing of the carfusion dataset.
It is divided into 5 parts:

## Installation of the prerequisites

First and foremost, lets install the prerequisites for this work, do:

pip install -r requirements.txt 

## Downloading of the data 

The samsung dataset is not yet public. It is a dataset produced for for the applications related to this project. For the people working in the VITA laboratory, the dataset is saved on the v100 under ```/data/bonnesoe-data/data/samsung/```. 

## Process the data 

To process the data of the samsung dataset, we need to open the notebook conversion_to_coco.ipynb which will convert our annotations to a COCO formatting. 
It will allow pifpaf to read those informations in order to process them. 
4 main parameters needs to be provided : 

-The train/test ratio and the train/val ratio ```train_test_ratio``` and ```train_val_ratio```

- The path of the scenes of the samsung dataset ```scenes_dir``` (be sure that there is no zip files in this folder).

- The path of the annotations files (they are json files) of the samsung dataset ```annotations_dir``` .

- The ```output_dir``` of your annotations and their name in the list ```jsons```.


## Visualize your data

Finally, to vizualize The processed data, a visualizer notebook is provided. To use it, put your processed jsons files in the variable ```jsons_files```  and the ```ann_folder``` at the begining of the document then run the notebook.