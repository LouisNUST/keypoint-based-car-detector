export LE=800

CUDA_VISIBLE_DEVICES=${CUDA_DEVI} python3 -m openpifpaf.predict   --paf-th 0.05 --seed-threshold 0.5 --instance-threshold 0.1 --checkpoint ${MODEL}  /data/bonnesoeur-data/visu_nuscenes/CAM_FRONT/*.jpg  -o /data/bonnesoeur-data/visu_nuscenes/SE${SE}_all/LE${LE}/nuscenes/ --long-edge ${LE} --force-complete-pose

export LE=420

CUDA_VISIBLE_DEVICES=${CUDA_DEVI} python3 -m openpifpaf.predict   --paf-th 0.05 --seed-threshold 0.5 --instance-threshold 0.1 --checkpoint ${MODEL}  /data/bonnesoeur-data/visu_nuscenes/CAM_FRONT/*.jpg  -o /data/bonnesoeur-data/visu_nuscenes/SE${SE}_all/LE${LE}/nuscenes/ --long-edge ${LE} --force-complete-pose




CUDA_VISIBLE_DEVICES=${CUDA_DEVI} python3 -m openpifpaf.predict   --paf-th 0.05 --seed-threshold 0.5 --instance-threshold 0.1 --checkpoint ${MODEL}  /data/bonnesoeur-data/visu_nuscenes/CAM_FRONT/*.jpg  -o /data/bonnesoeur-data/visu_nuscenes/SE${SE}_all/NO_LE/nuscenes/ --force-complete-pose

export LE=1200

CUDA_VISIBLE_DEVICES=${CUDA_DEVI} python3 -m openpifpaf.predict   --paf-th 0.05 --seed-threshold 0.5 --instance-threshold 0.1 --checkpoint ${MODEL}  /data/bonnesoeur-data/visu_nuscenes/CAM_FRONT/*.jpg  -o /data/bonnesoeur-data/visu_nuscenes/SE${SE}_all/LE${LE}/nuscenes/ --long-edge ${LE} --force-complete-pose