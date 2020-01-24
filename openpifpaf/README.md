# openpifpaf


> We propose a new bottom-up method for multi-car 2D human pose
> estimation that is particularly well suited for urban mobility such as self-driving cars
> and delivery robots. The new method, PifPaf, uses a Part Intensity Field (PIF) to
> localize body parts and a Part Association Field (PAF) to associate car parts with each other to form
> full car skeleton.
> Our method outperforms previous methods at low resolution and in crowded,
> cluttered and occluded scenes
> thanks to (i) our new composite field PAF encoding fine-grained information and (ii) the choice of Laplace loss for regressions which incorporates a notion of uncertainty.
> Our architecture is based on a fully
> convolutional, single-shot, box-free design.

# Openpifpaf for cars (and as many thinks as you want)

# Introduction

This work is part of a project aiming to detect cars with the openpifpaf framework by creating a skeleton arounf the frames of the cars. This leaded to turn the [original code](https://github.com/vita-epfl/openpifpaf) and to generalize it to any kind of dataset.


![Carfusion validation](docs/validation.png)

![Carfusion nuscenes](docs/nuscenes.png)


# Install

Python 3 is required. Python 2 is not supported.
Do not clone this repository
and make sure there is no folder named `openpifpaf` in your current directory.

```sh
pip3 install openpifpaf
```

For development of the openpifpaf source code itself, you need to clone this repository and then:

```sh
pip3 install numpy cython
pip3 install --editable '.[train,test]'
```

The last command installs the Python package in the current directory
(signified by the dot) with the optional dependencies needed for training and
testing.

# To modify

A few modification needs to be done nonetheless in three functions of pifpaf:

* data.py
* dataset.py
* evalcoco.py

Also, one needs to feed a dataset that was preprocessed in the coco format to be able to train this algortihtm. An example of this is provided with the processed dataset of [carFusion](http://www.cs.cmu.edu/~mvo/index_files/Papers/CarFusion.pdf) preprocessed to fit the [formatting](https://github.com/peterbonnesoeur/keypoint-based-car-detector/tree/master/carfusion_to_coco). 

- **Data.py**

In data.py, the name of the supercategory 'data_category' has to be modified with the name of the supercategory of your dataset.Furthermore, the desired Skeleton, Keypoints and hflip and Sigmas (used for the loss function) have to set the parameters : 'COCO_SKELETON', 'COCO_KEYPOINTS', 'HFLIP' and 'COCO_SIGMAS'.[If you wnaz to use carfusion for humans/cars, just replace those values with the ones with 'PERSON' or 'CAR' present in the document]. 
- **Dataset.py**
In dataset.py, containing the images of your dataset and the annotation directory have to be set.

- **Eval_coco**
In eval_coco.py, set the name of the annotations and image directory for the validation of the dataset.

--- 

# Training 

!
___

```
@InProceedings{kreiss2019pifpaf,
  author = {Kreiss, Sven and Bertoni, Lorenzo and Alahi, Alexandre},
  title = {PifPaf: Composite Fields for Human Pose Estimation},
  booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  month = {June},
  year = {2019}
}
```

[CVPR 2019 website](http://openaccess.thecvf.com/content_CVPR_2019/html/Kreiss_PifPaf_Composite_Fields_for_Human_Pose_Estimation_CVPR_2019_paper.html),
[arxiv.org/abs/1903.06593](https://arxiv.org/abs/1903.06593)



# Interfaces

* `python3 -m openpifpaf.predict --help`: [help screen](docs/cli-help-predict.txt)
* `python3 -m openpifpaf.webcam --help`: [help screen](docs/cli-help-webcam.txt)
* `python3 -m openpifpaf.train --help`: [help screen](docs/cli-help-train.txt)
* `python3 -m openpifpaf.eval_coco --help`: [help screen](docs/cli-help-eval_coco.txt)
* `python3 -m openpifpaf.logs --help`: [help screen](docs/cli-help-logs.txt)

Tools to work with models:

* `python3 -m openpifpaf.migrate --help`: [help screen](docs/cli-help-migrate.txt)
* `python3 -m openpifpaf.export_onnx --help`: [help screen](docs/cli-help-export_onnx.txt)


# Pre-trained Models

Performance metrics with on the carfusion training set are obtained with a TITAN graphics cards:

| Backbone        | AP       |  AR       | t_{total} [ms]  | t_{dec} [ms] | long_edges | Square_edges |
|----------------:|:--------:|:---------:|:---------------:|:------------:|:----------:|:------------:|
| resnet101       | __68.5__ | 70.1      |     521         | 257          |1800        |   250        |
| resnet101       | __69.5__ | 70.9      |     518         | 255          |1800        |   420        |
| resnet101       | __70.0__ | 71.4      |     440         | 233          |1800        |   800        |


Pretrained model files are shared in the releases : 
__[Github](https://github.com/peterbonnesoeur/keypoint-based-car-detector/releases)__
which you can put into your `outputs` folder.
To use the pretrained models, use their name when the checkpoint is needed with (--checkpoint 'name_package'.pkl).

To visualize logs:

```sh
python3 -m openpifpaf.logs \
  outputs/resnet50block5-pif-paf-edge401-190424-122009.pkl.log \
  outputs/resnet101block5-pif-paf-edge401-190412-151013.pkl.log \
  outputs/resnet152block5-pif-paf-edge401-190412-121848.pkl.log
```


# Train

See [datasets](docs/datasets.md) for setup instructions.
See [studies.ipynb](docs/studies.ipynb) for previous studies.

The exact training command that was used for a model is in the first
line of the training log file.

**IMPORTANT**

Before training, please take a look at 2 factors : the random rescaling of the images (*train.py [transforms.RescaleRelative - line 119]*) and the data augmentation parameters(*transforms.py [Train_TRANSFORM - line 598]*). Those parameters greatly influence the final results of your training and can be tunned to optimize their results for a peculiar application.

Train a ResNet model:

```sh
time CUDA_VISIBLE_DEVICES=0,1 python3 -m openpifpaf.train \
  --batch-size=8 \
  --loader-workers=8 \
  --basenet=resnet50block5 \
  --head-quad=1 \
  --headnets pif paf \
  --lr=1e-3 \
  --momentum=0.95 \
  --epochs=75 \
  --lr-decay 60 70 \
  --lambdas 30 2 2 50 3 3 \
  --freeze-base=1
```

ShuffleNet models are trained without ImageNet pretraining:

```sh
time CUDA_VISIBLE_DEVICES=0,1 python3 -m openpifpaf.train \
  --batch-size=64 \
  --loader-workers=8 \
  --basenet=shufflenetv2x2 \
  --head-quad=1 \
  --headnets pif paf \
  --lr=1e-1 \
  --momentum=0.9 \
  --epochs=75 \
  --lr-decay 60 70 \
  --lambdas 30 2 2 50 3 3 \
  --no-pretrain \
  --weight-decay=1e-5 \
  --update-batchnorm-runningstatistics \
  --ema=0.03
```


The command used to train our models was the following one :


```sh
time CUDA_VISIBLE_DEVICES=0,1 python3 -m openpifpaf.train 
  --lr=1e-3  
  --momentum=0.95  
  --epochs=50   
  --lr-decay 35  
  --basenet=resnet101  
  --headnets pif paf skeleton  
  --square-edge=420       (or 250, or 800)
  --rescale-images 1.0
```

You can refine an existing model with the `--checkpoint` option.

It is now also possible to use a previous pretrained model for a peculair kind a skeleton (for example, with 14 keypoints) to train a new model with a different sumber of keypoints (for example 17). To do so, just add the command checkpoint during your training to use the pretrained model desired:

```sh
time CUDA_VISIBLE_DEVICES=0,1 python3 -m openpifpaf.train 
  --lr=1e-3  
  --momentum=0.95  
  --epochs=50   
  --lr-decay 35  
  --basenet=resnet101  
  --headnets pif paf skeleton  
  --square-edge=420       (or 250, or 800)
  --rescale-images 1.0
```

In this case, the value in 'basenet' will be the name of the trained model.


# Video

Processing a video frame by frame from `video.avi` to `video.pose.mp4` using ffmpeg:

```sh
export VIDEO=video.avi  # change to your video file

mkdir ${VIDEO}.images
ffmpeg -i ${VIDEO} -qscale:v 2 -vf scale=641:-1 -f image2 ${VIDEO}.images/%05d.jpg
python3 -m openpifpaf.predict --checkpoint resnet152 --glob "${VIDEO}.images/*.jpg"
ffmpeg -framerate 24 -pattern_type glob -i ${VIDEO}.images/'*.jpg.skeleton.png' -vf scale=640:-2 -c:v libx264 -pix_fmt yuv420p ${VIDEO}.pose.mp4
```

In this process, ffmpeg scales the video to `641px` which can be adjusted.


# Documentation Pages

* [datasets](docs/datasets.md)
* [Google Colab demo](https://colab.research.google.com/drive/1H8T4ZE6wc0A9xJE4oGnhgHpUpAH5HL7W)
* [studies.ipynb](docs/studies.ipynb)
* [evaluation logs](docs/eval_logs.md)
* [performance analysis](docs/performance.md)
* [history](HISTORY.md)
* [contributing](CONTRIBUTING.md)


# Related Projects

* [monoloco](https://github.com/vita-epfl/monoloco): "Monocular 3D Pedestrian Localization and Uncertainty Estimation" which uses OpenPifPaf for poses.
* [openpifpafwebdemo](https://github.com/vita-epfl/openpifpafwebdemo): web front-end.


[CC-BY-2.0]: https://creativecommons.org/licenses/by/2.0/

------