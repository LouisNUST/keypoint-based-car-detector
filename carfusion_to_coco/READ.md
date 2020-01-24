# Carfusion Downloading and processing

This part of the code is dedicated to the download and processing of the carfusion dataset.
It is divided into 5 parts:

## Installation of the prerequisites

First and foremost, lets install the prerequisites for this work, do:

pip install -r requirements.txt 

# Download yolov3

For the processing, you need to download the [yolo](https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5) package to identify the non annotated cars in the dataset.
Then, place the package in the 'model' folder.

It can also be installed with :

wget -P ./model https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5

## Downloading of the carfusion dataset

Then, we need to download the carfusion dataset. The script ' downlad_carfusion ' is there for this purpose. 
feel free to modify the destination of the dataset by modifying the 'dest_path' of the file. Then, run it with : 

python downlad_carfusion.py

Be carefull to remove the zip files if it is not done automatically

## Process the data 

To process the data of the 