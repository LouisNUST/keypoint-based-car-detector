
import numpy as np


COCO_KEYPOINTS = [
    'front_left_wheel',         #1          0
    'front_right_wheel',        #2          1
    'back_left_wheel',          #3          2
    'back_right_wheel',         #4          3
    'front_left_light',         #5          4
    'front_right_light',        #6          5
    'back_left_light',          #7          6
    'back_right_light',         #8          7
    'left_mirror',              #9          8
    'right_mirror',             #10         9
    'upper_left_windshield',    #11         10
    'upper_right_windshield',   #12         11
    'upper_left_rear',          #13         12
    'upper_right_rear',         #14         13
]

#? Keypoints for the cars
COCO_KEYPOINTS_CAR = [
    'front_left_wheel',         #1          0
    'front_right_wheel',        #2          1
    'back_left_wheel',          #3          2
    'back_right_wheel',         #4          3
    'front_left_light',         #5          4
    'front_right_light',        #6          5
    'back_left_light',          #7          6
    'back_right_light',         #8          7
    'left_mirror',              #9          8
    'right_mirror',             #10         9
    'upper_left_windshield',    #11         10
    'upper_right_windshield',   #12         11
    'upper_left_rear',          #13         12
    'upper_right_rear',         #14         13
]

#? Keypoints for the humans
COCO_KEYPOINTS_PERSON = [
    'nose',            # 1
    'left_eye',        # 2
    'right_eye',       # 3
    'left_ear',        # 4
    'right_ear',       # 5
    'left_shoulder',   # 6
    'right_shoulder',  # 7
    'left_elbow',      # 8
    'right_elbow',     # 9
    'left_wrist',      # 10
    'right_wrist',     # 11
    'left_hip',        # 12
    'right_hip',       # 13
    'left_knee',       # 14
    'right_knee',      # 15
    'left_ankle',      # 16
    'right_ankle',     # 17
]


HFLIP = {
    'front_left_wheel' :'front_right_wheel',
    'back_left_wheel' : 'back_right_wheel',
    'front_left_light' : 'front_right_light',
    'back_left_light' : 'back_right_light',
    'left_mirror' : 'right_mirror',
    'upper_left_windshield' : 'upper_right_windshield',
    'upper_left_rear' : 'upper_right_rear',
}


#? hflip for the cars
HFLIP_CAR = {
    'front_left_wheel' :'front_right_wheel',
    'back_left_wheel' : 'back_right_wheel',
    'front_left_light' : 'front_right_light',
    'back_left_light' : 'back_right_light',
    'left_mirror' : 'right_mirror',
    'upper_left_windshield' : 'upper_right_windshield',
    'upper_left_rear' : 'upper_right_rear',
}

#? hflip for the humans
HFLIP_PERSON = {
    'left_eye': 'right_eye',
    'right_eye': 'left_eye',
    'left_ear': 'right_ear',
    'right_ear': 'left_ear',
    'left_shoulder': 'right_shoulder',
    'right_shoulder': 'left_shoulder',
    'left_elbow': 'right_elbow',
    'right_elbow': 'left_elbow',
    'left_wrist': 'right_wrist',
    'right_wrist': 'left_wrist',
    'left_hip': 'right_hip',
    'right_hip': 'left_hip',
    'left_knee': 'right_knee',
    'right_knee': 'left_knee',
    'left_ankle': 'right_ankle',
    'right_ankle': 'left_ankle',
}


def transform_keypoints(keypoints, mode):

    assert mode == 'flip', "mode not recognized"
    kps = np.array(keypoints)
    dic_kps = {key: kps[:, :, idx] for idx, key in enumerate(COCO_KEYPOINTS)}
    kps_hflip = np.array([dic_kps[value] for key, value in HFLIP.items()])
    kps_hflip = np.transpose(kps_hflip, (1, 2, 0))
    return kps_hflip.tolist()
