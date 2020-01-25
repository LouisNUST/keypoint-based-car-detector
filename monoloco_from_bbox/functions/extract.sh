for filename in *.tgz
mkdir nuscenes
do
  tar -xvzf $filename -C ./nuscenes/ --keep-old-files
done
