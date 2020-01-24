
export POS=CAM_BACK

CUDA_VISIBLE_DEVICES=${CUDA_DEVI} python3 -m openpifpaf.predict   --paf-th 0.05 --seed-threshold 0.5 --instance-threshold 0.1 --checkpoint ${MODEL}  /data/bonnesoeur-data/data/nuscenes/samples/${POS}/*.jpg  -o /data/bonnesoeur-data/monoloco/car_nuscenes/json/in --output-types json --long-edge ${LE} --force-complete-pose

export POS=CAM_BACK_LEFT

CUDA_VISIBLE_DEVICES=${CUDA_DEVI} python3 -m openpifpaf.predict   --paf-th 0.05 --seed-threshold 0.5 --instance-threshold 0.1 --checkpoint ${MODEL}  /data/bonnesoeur-data/data/nuscenes/samples/${POS}/*.jpg  -o /data/bonnesoeur-data/monoloco/car_nuscenes/json/in --output-types json --long-edge ${LE} --force-complete-pose

export POS=CAM_BACK_RIGHT

CUDA_VISIBLE_DEVICES=${CUDA_DEVI} python3 -m openpifpaf.predict   --paf-th 0.05 --seed-threshold 0.5 --instance-threshold 0.1 --checkpoint ${MODEL}  /data/bonnesoeur-data/data/nuscenes/samples/${POS}/*.jpg  -o /data/bonnesoeur-data/monoloco/car_nuscenes/json/in --output-types json --long-edge ${LE} --force-complete-pose

export POS=CAM_FRONT

CUDA_VISIBLE_DEVICES=${CUDA_DEVI} python3 -m openpifpaf.predict   --paf-th 0.05 --seed-threshold 0.5 --instance-threshold 0.1 --checkpoint ${MODEL}  /data/bonnesoeur-data/data/nuscenes/samples/${POS}/*.jpg  -o /data/bonnesoeur-data/monoloco/car_nuscenes/json/in --output-types json --long-edge ${LE} --force-complete-pose

export POS=CAM_FRONT_RIGHT

CUDA_VISIBLE_DEVICES=${CUDA_DEVI} python3 -m openpifpaf.predict   --paf-th 0.05 --seed-threshold 0.5 --instance-threshold 0.1 --checkpoint ${MODEL}  /data/bonnesoeur-data/data/nuscenes/samples/${POS}/*.jpg  -o /data/bonnesoeur-data/monoloco/car_nuscenes/json/in --output-types json --long-edge ${LE} --force-complete-pose

export POS=CAM_FRONT_LEFT

CUDA_VISIBLE_DEVICES=${CUDA_DEVI} python3 -m openpifpaf.predict   --paf-th 0.05 --seed-threshold 0.5 --instance-threshold 0.1 --checkpoint ${MODEL}  /data/bonnesoeur-data/data/nuscenes/samples/${POS}/*.jpg  -o /data/bonnesoeur-data/monoloco/car_nuscenes/json/in --output-types json --long-edge ${LE} --force-complete-pose




