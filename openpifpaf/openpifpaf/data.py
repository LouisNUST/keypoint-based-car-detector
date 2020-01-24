import numpy as np

#Carfusion dataset

#? Skeleton used by pifpaf

data_category = 'car'

COCO_SKELETON = [
    [1, 2], [1,3], [2,4], [3,4],    #wheels
    [1,5], [2,6],[3,7], [4,8],      #Links between the wheels and the lights
    [5,6], [7,8],                   #links between the lights
    [5,9], [6,10],                  #links between the mirrors and the front lights
    [5,11],[6,12], [7,13],[8,14],   #links between the lights and the windshiel/rear
    [11,12],[11,13],[12,14],[13,14] #links between the rear and the windshiel
]

COCO_CAR_SKELETON = [
    [1, 2], [1,3], [2,4], [3,4],    #wheels
    [1,5], [2,6],[3,7], [4,8],      #Links between the wheels and the lights
    [5,6], [7,8],                   #links between the lights
    [5,9], [6,10],                  #links between the mirrors and the front lights
    [5,11],[6,12], [7,13],[8,14],   #links between the lights and the windshiel/rear
    [11,12],[11,13],[12,14],[13,14] #links between the rear and the windshiel
]

COCO_PERSON_SKELETON = [
    (16, 14), (14, 12), (17, 15), (15, 13), (12, 13), (6, 12), (7, 13),
    (6, 7), (6, 8), (7, 9), (8, 10), (9, 11), (2, 3), (1, 2), (1, 3),
    (2, 4), (3, 5), (4, 6), (5, 7),
]

KINEMATIC_TREE_SKELETON = [
    (1, 2), (2, 4),  # left head
    (1, 3), (3, 5),
    (1, 6),
    (6, 8), (8, 10),  # left arm
    (1, 7),
    (7, 9), (9, 11),  # right arm
    (6, 12), (12, 14), (14, 16),  # left side
    (7, 13), (13, 15), (15, 17),
]

#W consider a link between the mirror and the front light of the cars


#? Keypoints for the humans
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


#? Flip functions

HFLIP = {
    'front_left_wheel' :'front_right_wheel',
    'back_left_wheel' : 'back_right_wheel',
    'front_left_light' : 'front_right_light',
    'back_left_light' : 'back_right_light',
    'left_mirror' : 'right_mirror',
    'upper_left_windshield' : 'upper_right_windshield',
    'upper_left_rear' : 'upper_right_rear',
}



HFLIP_CAR = {
    'front_left_wheel' :'front_right_wheel',
    'back_left_wheel' : 'back_right_wheel',
    'front_left_light' : 'front_right_light',
    'back_left_light' : 'back_right_light',
    'left_mirror' : 'right_mirror',
    'upper_left_windshield' : 'upper_right_windshield',
    'upper_left_rear' : 'upper_right_rear',
}

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


DENSER_COCO_PERSON_SKELETON = [
    (1, 2), (1, 3), (2, 3), (1, 4), (1, 5), (4, 5),
    (1, 6), (1, 7), (2, 6), (3, 7),
    (2, 4), (3, 5), (4, 6), (5, 7), (6, 7),
    (6, 12), (7, 13), (6, 13), (7, 12), (12, 13),
    (6, 8), (7, 9), (8, 10), (9, 11), (6, 10), (7, 11),
    (8, 9), (10, 11),
    (10, 12), (11, 13),
    (10, 14), (11, 15),
    (14, 12), (15, 13), (12, 15), (13, 14),
    (12, 16), (13, 17),
    (16, 14), (17, 15), (14, 17), (15, 16),
    (14, 15), (16, 17),
]


#? Sigmas for the loss and evaluation functions functions (Values for the evaluation with COCO) 

COCO_SIGMAS = [
    0.1,      #front wheel
    0.1,      #front wheel
    0.1,      #back wheel
    0.1,      #back wheel
    0.04,      #front light
    0.04,      #front light
    0.04,      #back light
    0.04,      #back light
    0.03,      #mirror
    0.03,      #mirror
    0.08,      #windshield
    0.08,      #windshield
    0.08,      #rear
    0.08,      #rear
]


COCO_CAR_SIGMAS = [
    0.1,      #front wheel
    0.1,      #front wheel
    0.1,      #back wheel
    0.1,      #back wheel
    0.04,      #front light
    0.04,      #front light
    0.04,      #back light
    0.04,      #back light
    0.03,      #mirror
    0.03,      #mirror
    0.08,      #windshield
    0.08,      #windshield
    0.08,      #rear
    0.08,      #rear
]

COCO_CAR_SIGMAS2 = [
    0.1,      #front wheel
    0.1,      #front wheel
    0.1,      #back wheel
    0.1,      #back wheel
    0.1,      #front light
    0.1,      #front light
    0.1,      #back light
    0.1,      #back light
    0.1,      #mirror
    0.1,      #mirror
    0.1,      #windshield
    0.1,      #windshield
    0.1,      #rear
    0.1,      #rear
]

COCO_PERSON_SIGMAS = [
    0.026,  # nose
    0.025,  # eyes
    0.025,  # eyes
    0.035,  # ears
    0.035,  # ears
    0.079,  # shoulders
    0.079,  # shoulders
    0.072,  # elbows
    0.072,  # elbows
    0.062,  # wrists
    0.062,  # wrists
    0.107,  # hips
    0.107,  # hips
    0.087,  # knees
    0.087,  # knees
    0.089,  # ankles
    0.089,  # ankles
]
# Should not modify this
def draw_skeletons():
    from . import show
    coordinates = np.array([[
        [0.0, 9.3, 2.0],  # 'nose',            # 1
        [-0.5, 9.7, 2.0],  # 'left_eye',        # 2
        [0.5, 9.7, 2.0],  # 'right_eye',       # 3
        [-1.0, 9.5, 2.0],  # 'left_ear',        # 4
        [1.0, 9.5, 2.0],  # 'right_ear',       # 5
        [-2.0, 8.0, 2.0],  # 'left_shoulder',   # 6
        [2.0, 8.0, 2.0],  # 'right_shoulder',  # 7
        [-2.5, 6.0, 2.0],  # 'left_elbow',      # 8
        [2.5, 6.2, 2.0],  # 'right_elbow',     # 9
        [-2.5, 4.0, 2.0],  # 'left_wrist',      # 10
        [2.5, 4.2, 2.0],  # 'right_wrist',     # 11
        [-1.8, 4.0, 2.0],  # 'left_hip',        # 12
        [1.8, 4.0, 2.0],  # 'right_hip',       # 13
        [-2.0, 2.0, 2.0],  # 'left_knee',       # 14
        [2.0, 2.1, 2.0],  # 'right_knee',      # 15
        [-2.0, 0.0, 2.0],  # 'left_ankle',      # 16
        [2.0, 0.1, 2.0],  # 'right_ankle',     # 17
    ]])

    keypoint_painter = show.KeypointPainter(show_box=False, color_connections=True,
                                            markersize=1, linewidth=6)

    with show.canvas('docs/skeleton_coco.png', figsize=(2, 5)) as ax:
        ax.set_axis_off()
        keypoint_painter.skeleton = COCO_SKELETON
        keypoint_painter.keypoints(ax, coordinates)

    with show.canvas('docs/skeleton_kinematic_tree.png', figsize=(2, 5)) as ax:
        ax.set_axis_off()
        keypoint_painter.skeleton = KINEMATIC_TREE_SKELETON
        keypoint_painter.keypoints(ax, coordinates)

    with show.canvas('docs/skeleton_dense.png', figsize=(2, 5)) as ax:
        ax.set_axis_off()
        keypoint_painter.skeleton = DENSER_COCO_PERSON_SKELETON
        keypoint_painter.keypoints(ax, coordinates)


def print_associations():
    for j1, j2 in COCO_SKELETON:
        print(COCO_KEYPOINTS[j1 - 1], '-', COCO_KEYPOINTS[j2 - 1])


if __name__ == '__main__':
    print_associations()
    draw_skeletons()
