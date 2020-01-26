# Carfusion Downloading and processing

This part of the code is dedicated to the download and processing of the carfusion dataset.
It is divided into 5 parts:

## Installation of the prerequisites

First and foremost, lets install the prerequisites for this work, do:

pip install -r requirements.txt 

# Download yolov3

For the processing, you need to download the [yolo](https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5) package to identify the non annotated cars in the dataset.
Then, place the package in the ```model``` folder.

It can also be installed with :

wget -P ./model https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5

## Downloading of the carfusion dataset

Then, we need to download the carfusion dataset. The file ```downlad_carfusion.py``` is there for this purpose. 
feel free to modify the destination of the dataset by modifying the ```dest_path``` of the file. Then, run it with : 

python downlad_carfusion.py

Be carefull to remove the zip files if it is not done automatically

## Process the data 

To process the data of the carFusion dataset, we need to open the notebook conversion_to_coco.ipynb which will convert our annotations to a COCO formatting. 
It will allow pifpaf to read those informations in order to process them. 
3 main parameters needs to be providied : 

- The path of the carfusion dataset ```dir_carfusion``` (be sure that there is no zip files in this folder).

- The ```IOU``` thresholding (default = 0.3) to detect the cars not annotated in the carfusion dataset (More explanations in the notebook).

- The type of detection ```car_only``` (default = False) (wether it should detect only car)s or trucks and vans as well).

## Visualize your data

Finally, to vizualize The processed data, a visualizer notebook is provided. To use it, put your processed jsons files in the vraible ```jsons``` then run the notebook.