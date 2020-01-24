CUDA_VISIBLE_DEVICES=${CUDA_DEVI} python3 -m openpifpaf.predict   --paf-th 0.05 --seed-threshold 0.5 --instance-threshold 0.1 --checkpoint ${MODEL}  /data/bonnesoeur-data/visu_nuscenes/CAM_FRONT/*.jpg  -o /data/bonnesoeur-data/visu_nuscenes/SE${SE}/NO_LE/nuscenes/ 

CUDA_VISIBLE_DEVICES=${CUDA_DEVI} python3 -m openpifpaf.predict   --paf-th 0.05 --seed-threshold 0.5 --instance-threshold 0.1 --checkpoint ${MODEL}  /data/bonnesoeur-data/data/carfusion/test/car_penn1/images_jpg/10*.jpg  -o /data/bonnesoeur-data/visu_nuscenes/SE${SE}/NO_LE/validation/

CUDA_VISIBLE_DEVICES=${CUDA_DEVI} python3 -m openpifpaf.predict   --paf-th 0.05 --seed-threshold 0.5 --instance-threshold 0.1 --checkpoint ${MODEL}  /data/bonnesoeur-data/data/carfusion/train/car_butler1/images_jpg/11*.jpg  -o /data/bonnesoeur-data/visu_nuscenes/SE${SE}/NO_LE/training/

CUDA_VISIBLE_DEVICES=${CUDA_DEVI} python3 -m openpifpaf.predict   --paf-th 0.1 --seed-threshold 0.5 --instance-threshold 0.1 --checkpoint ${MODEL}  /home/bonnesoe/semester_project/monoloco/data/kitti/images/0000*.png  -o /data/bonnesoeur-data/visu_nuscenes/SE${SE}/NO_LE/kitti/

export LE=1200

CUDA_VISIBLE_DEVICES=${CUDA_DEVI} python3 -m openpifpaf.predict   --paf-th 0.05 --seed-threshold 0.5 --instance-threshold 0.1 --checkpoint ${MODEL}  /data/bonnesoeur-data/visu_nuscenes/CAM_FRONT/*.jpg  -o /data/bonnesoeur-data/visu_nuscenes/SE${SE}/LE${LE}/nuscenes/ --long-edge ${LE}

CUDA_VISIBLE_DEVICES=${CUDA_DEVI} python3 -m openpifpaf.predict   --paf-th 0.05 --seed-threshold 0.5 --instance-threshold 0.1 --checkpoint ${MODEL}  /data/bonnesoeur-data/data/carfusion/train/car_butler1/images_jpg/11*.jpg  -o /data/bonnesoeur-data/visu_nuscenes/SE${SE}/LE${LE}/training/ --long-edge ${LE}

CUDA_VISIBLE_DEVICES=${CUDA_DEVI} python3 -m openpifpaf.predict   --paf-th 0.05 --seed-threshold 0.5 --instance-threshold 0.1 --checkpoint ${MODEL}  /data/bonnesoeur-data/data/carfusion/test/car_penn1/images_jpg/10*.jpg  -o /data/bonnesoeur-data/visu_nuscenes/SE${SE}/LE${LE}/validation/ --long-edge ${LE}

CUDA_VISIBLE_DEVICES=${CUDA_DEVI} python3 -m openpifpaf.predict   --paf-th 0.1 --seed-threshold 0.5 --instance-threshold 0.1 --checkpoint ${MODEL}  /home/bonnesoe/semester_project/monoloco/data/kitti/images/0000*.png  -o /data/bonnesoeur-data/visu_nuscenes/SE${SE}/LE${LE}/kitti/  --long-edge ${LE}


export LE=800

CUDA_VISIBLE_DEVICES=${CUDA_DEVI} python3 -m openpifpaf.predict   --paf-th 0.05 --seed-threshold 0.5 --instance-threshold 0.1 --checkpoint ${MODEL}  /data/bonnesoeur-data/visu_nuscenes/CAM_FRONT/*.jpg  -o /data/bonnesoeur-data/visu_nuscenes/SE${SE}/LE${LE}/nuscenes/ --long-edge ${LE}

CUDA_VISIBLE_DEVICES=${CUDA_DEVI} python3 -m openpifpaf.predict   --paf-th 0.05 --seed-threshold 0.5 --instance-threshold 0.1 --checkpoint ${MODEL}  /data/bonnesoeur-data/data/carfusion/train/car_butler1/images_jpg/11*.jpg  -o /data/bonnesoeur-data/visu_nuscenes/SE${SE}/LE${LE}/training/ --long-edge ${LE}

CUDA_VISIBLE_DEVICES=${CUDA_DEVI} python3 -m openpifpaf.predict   --paf-th 0.05 --seed-threshold 0.5 --instance-threshold 0.1 --checkpoint ${MODEL}  /data/bonnesoeur-data/data/carfusion/test/car_penn1/images_jpg/10*.jpg  -o /data/bonnesoeur-data/visu_nuscenes/SE${SE}/LE${LE}/validation/ --long-edge ${LE}

CUDA_VISIBLE_DEVICES=${CUDA_DEVI} python3 -m openpifpaf.predict   --paf-th 0.1 --seed-threshold 0.5 --instance-threshold 0.1 --checkpoint ${MODEL}  /home/bonnesoe/semester_project/monoloco/data/kitti/images/0000*.png  -o /data/bonnesoeur-data/visu_nuscenes/SE${SE}/LE${LE}/kitti/  --long-edge ${LE}


export LE=420

CUDA_VISIBLE_DEVICES=${CUDA_DEVI} python3 -m openpifpaf.predict   --paf-th 0.05 --seed-threshold 0.5 --instance-threshold 0.1 --checkpoint ${MODEL}  /data/bonnesoeur-data/visu_nuscenes/CAM_FRONT/*.jpg  -o /data/bonnesoeur-data/visu_nuscenes/SE${SE}/LE${LE}/nuscenes/ --long-edge ${LE}

CUDA_VISIBLE_DEVICES=${CUDA_DEVI} python3 -m openpifpaf.predict   --paf-th 0.05 --seed-threshold 0.5 --instance-threshold 0.1 --checkpoint ${MODEL}  /data/bonnesoeur-data/data/carfusion/train/car_butler1/images_jpg/11*.jpg  -o /data/bonnesoeur-data/visu_nuscenes/SE${SE}/LE${LE}/training/ --long-edge ${LE}

CUDA_VISIBLE_DEVICES=${CUDA_DEVI} python3 -m openpifpaf.predict   --paf-th 0.05 --seed-threshold 0.5 --instance-threshold 0.1 --checkpoint ${MODEL}  /data/bonnesoeur-data/data/carfusion/test/car_penn1/images_jpg/10*.jpg  -o /data/bonnesoeur-data/visu_nuscenes/SE${SE}/LE${LE}/validation/ --long-edge ${LE}

CUDA_VISIBLE_DEVICES=${CUDA_DEVI} python3 -m openpifpaf.predict   --paf-th 0.1 --seed-threshold 0.5 --instance-threshold 0.1 --checkpoint ${MODEL}  /home/bonnesoe/semester_project/monoloco/data/kitti/images/0000*.png  -o /data/bonnesoeur-data/visu_nuscenes/SE${SE}/LE${LE}/kitti/  --long-edge ${LE}
