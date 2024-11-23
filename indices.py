# Mesh Landmarks
MESH_CONNECTIONS = {
    # Background placeholder
    "BACKGROUND": [],

    # Face connections
    "FACE": [10, 109, 67, 103, 54, 21, 162, 127, 234, 93, 132, 58, 172, 136, 150, 149, 176, 148, 152, 377, 400, 378, 379, 365, 397, 288, 361, 323, 454, 356, 389, 251, 284, 332, 332, 297, 338, 10],
    "INNER_MOUTH": [11, 72, 73, 74, 62, 180, 85, 315, 404, 320, 307, 408, 272, 271, 12],

    "LEFT_EYEBROW": [295, 282, 283, 276, 300, 293, 334, 296, 336, 285],
    "RIGHT_EYEBROW": [65, 52, 53, 46, 70, 63, 105, 66, 107, 55],

    "LEFT_EYEWHITE": [33, 246, 161, 160, 159, 158, 157, 173, 133, 155, 154, 153, 145, 144, 163],
    "RIGHT_EYEWHITE": [263, 466, 388, 387, 386, 385, 384, 398, 362, 382, 381, 380, 373, 390],
    "RIGHT_PUPIL": [468,471],
    "LEFT_PUPIL": [473, 476],
    "LEFT_EYELID": [263, 467, 260, 257, 258, 286, 414, 463, 398, 384, 385, 386, 387, 388],
    "RIGHT_EYELID": [173, 56, 28, 27, 29, 30, 247, 130, 161, 160, 159, 158, 157, 173],
    "B_LEFT_EYELID": [133, 155, 154, 153, 145, 144, 163, 130, 228, 229, 230],
    "B_RIGHT_EYELID": [362, 382, 381, 374, 390, 249, 263, 448, 450, 451, 452],
    "U_TEETH": [80, 81, 82, 13, 312, 311, 310],
    "B_TEETH": [178, 86, 14, 317, 402],
    "TOP_LIP": [76, 185, 40, 39, 37, 0, 267, 270, 409, 291, 308, 415, 310, 311, 312, 13, 82, 81, 80, 191, 78, 76],
    "BOTTOM_LIP": [78, 95, 178, 87, 14, 317, 317, 402, 318, 324, 308, 291, 375, 320, 404, 315, 16, 85, 180, 146, 76],
    "RIGHT_NOSE": [168, 122, 236, 131, 49, 102, 64, 235, 59, 166, 79, 238, 241, 141, 94],
    "LEFT_NOSE": [168, 351, 456, 360, 279, 331, 294, 455, 289, 392, 309, 458, 461, 370, 94],
    #"RIGHT_EAR": [234, 93],
    #"LEFT_EAR": [454, 323],

    # Hand connections
    "HAND_PALM": [0, 1, 2, 5, 9, 13, 17, 0],
    "HAND_THUMB": [1, 2, 3, 4],
    "HAND_POINTER": [5, 6, 7, 8],
    "HAND_MIDDLE": [9, 10, 11, 12],
    "HAND_RING": [13, 14, 15, 16],
    "HAND_PINKY": [17, 18, 19, 20]
}

# Hair types
HAIRSTYLES = {
    "MAN_SHORT": []
}

# Color pallettes
PALETTES = {
    "Caucasian":{
        # Background color
        "BACKGROUND": (255, 255, 255),

        # Face colors
        "FACE": (68, 163, 249),
        "INNER_MOUTH": (0,0,0),
        "LEFT_EYEWHITE": (255,255,255),
        "LEFT_EYEBROW": (4, 75, 140),
        "RIGHT_EYEBROW": (4, 75, 140),
        "RIGHT_EYEWHITE": (255,255,255),
        "RIGHT_PUPIL": (255,0,0),
        "LEFT_PUPIL": (255,0,0),
        "LEFT_EYELID": (68, 163, 249),
        "RIGHT_EYELID": (68, 163, 249),
        "B_LEFT_EYELID": (68, 163, 249),
        "B_RIGHT_EYELID": (68, 163, 249),
        "U_TEETH": (255,255,255),
        "B_TEETH": (255,255,255),
        "TOP_LIP": (128,128,255),
        "BOTTOM_LIP": (128,128,255),
        "RIGHT_NOSE": (35, 147, 248),
        "LEFT_NOSE": (35, 147, 248),

        # Hand colors
        "HAND_PALM": (0, 0, 0),
        "HAND_THUMB": (0, 0, 0),
        "HAND_POINTER": (0, 0, 0),
        "HAND_MIDDLE": (0, 0, 0),
        "HAND_RING": (0, 0, 0),
        "HAND_PINKY": (0, 0, 0)
    },
    "Creepy_mask":{
        # Background color
        "BACKGROUND": (0, 0, 0),

        # Face colors
        "FACE": (255,255,255),
        "INNER_MOUTH": (0, 0, 0),
        "LEFT_EYEWHITE": (0, 0, 0),
        "LEFT_EYEBROW": (255,255,255),
        "RIGHT_EYEBROW": (255,255,255),
        "RIGHT_EYEWHITE": (0, 0, 0),
        "RIGHT_PUPIL": (255,0,0),
        "LEFT_PUPIL": (255,0,0),
        "LEFT_EYELID": (255,255,255),
        "RIGHT_EYELID": (255,255,255),
        "B_LEFT_EYELID": (255,255,255),
        "B_RIGHT_EYELID": (255,255,255),
        "U_TEETH": (255,255,255),
        "B_TEETH": (255,255,255),
        "TOP_LIP": (255,255,255),
        "BOTTOM_LIP": (255,255,255),
        "RIGHT_NOSE": (190, 190, 190),
        "LEFT_NOSE": (190, 190, 190),

        # Hand colors
        "HAND_PALM": (255,255,255),
        "HAND_THUMB": (255,255,255),
        "HAND_POINTER": (255,255,255),
        "HAND_MIDDLE": (255,255,255),
        "HAND_RING": (255,255,255),
        "HAND_PINKY": (255,255,255)
    }
}