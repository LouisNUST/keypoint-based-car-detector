from google_drive_downloader import GoogleDriveDownloader as gdd

# Modify the paths to change the destination of the dataset

from google_drive_downloader import GoogleDriveDownloader as gdd
import os

file_ids = ['1L2azKaYabCQ0YWwGTnN0_uhNgnlACigM', '1Z15rX038FyRW62DOPEJW16bZZIj8LPC0', '1W0Ty7vZbnAGyvf0RNeVXcNJV6e7kcqzZ', '1T253FkwEfKEJyegHNztRPQX_bSjZUznf',
           '1uuDYPidIztuOHbDbP2hQv_ocGAnWPbGJ', '1R3xpUKjHPFOlOj8SZIV9hmtndFMw95iX',  '1goDsHDSU5dkJFoy0phTFD2brXf4Ou6sL',  '1AOFQrLQTkNs1djnfI7y-ZeeZQeqnHNQK',
           '1dYqJtokx1pMEtWH8XK9b_R481jv2ypn2', '12vSzUh_e3oMYVKewUeEzn9Gv3P_wnGYi']

paths = ['./datasets/carfusion/train/car_craig1.zip','./datasets/carfusion/train/car_craig2.zip', './datasets/carfusion/train/car_fifth1.zip', './datasets/carfusion/train/car_fifth2.zip',
         './datasets/carfusion/train/car_morewood1.zip', './datasets/carfusion/train/car_morewood2.zip',  './datasets/carfusion/train/car_butler1.zip', './datasets/carfusion/train/car_butler2.zip',
         './datasets/carfusion/test/car_penn1.zip','./datasets/carfusion/test/car_penn2.zip']

for path, file_id in zip(paths, file_ids) : 
    gdd.download_file_from_google_drive(file_id=file_id,
                                        dest_path=path,
                                        unzip=True,
                                        showsize=True,
                                        overwrite=True)
    os.remove(path) #Remove the zip files