CUDA_VISIBLE_DEVICES=${CUDA_DEVI} python3 -m openpifpaf.predict   --paf-th 0.05 --seed-threshold 0.5 --instance-threshold 0.1 --checkpoint ${MODEL}  /home/bonnesoe/semester_project/monoloco/data/kitti/images/0000*.png  -o /data/bonnesoeur-data/visu_nuscenes/SE${SE}/NO_LE/kitti/

export LE=1200
CUDA_VISIBLE_DEVICES=${CUDA_DEVI} python3 -m openpifpaf.predict   --paf-th 0.05 --seed-threshold 0.5 --instance-threshold 0.1 --checkpoint ${MODEL}  /home/bonnesoe/semester_project/monoloco/data/kitti/images/0000*.png  -o /data/bonnesoeur-data/visu_nuscenes/SE${SE}/LE${LE}/kitti/ 

export LE=800
CUDA_VISIBLE_DEVICES=${CUDA_DEVI} python3 -m openpifpaf.predict   --paf-th 0.05 --seed-threshold 0.5 --instance-threshold 0.1 --checkpoint ${MODEL}  /home/bonnesoe/semester_project/monoloco/data/kitti/images/0000*.png  -o /data/bonnesoeur-data/visu_nuscenes/SE${SE}/LE${LE}/kitti/ 

export LE=420
CUDA_VISIBLE_DEVICES=${CUDA_DEVI} python3 -m openpifpaf.predict   --paf-th 0.05 --seed-threshold 0.5 --instance-threshold 0.1 --checkpoint ${MODEL}  /home/bonnesoe/semester_project/monoloco/data/kitti/images/0000*.png  -o /data/bonnesoeur-data/visu_nuscenes/SE${SE}/LE${LE}/kitti/ 
