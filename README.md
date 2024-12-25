# MimicMe
A digital avatar implementation, based off MediaPipe

## About
- This is a digital avatar implementation using MediaPipe for mapping the avatar to faces
- It tracks facial features, and hands, and includes a simple GUI interface to alter these features
- Using TKinter for the GUI, MediaPipe for mapping, Cv2 for drawing, 
  and Pygame for rendering (using openGL allowing faster rendering speeds while window does not have rendering priority)
- Uses pyvirtualcam to send the avatar directly to a virtual OBS camera display, allowing use in applications such as zoom, discord, etc.
  (see https://pypi.org/project/pyvirtualcam/ for installation instructions)
  - Download OBS
  - Start up OBS
  - Click "Start Virtual Camera" (bottom right), then "Stop Virtual Camera"
  - Close OBS

## Running instructions
- Clone the repository, and run /build/main/main.exe
- Customize and enjoy with the tk GUI

## Creating coloring presets
- Open up indices.py, and create a new key in "PALETTES" attributed to a dictionary
  containing volor values in bgr format for each facial feature.

## Currently implemented features:
### Gui
- Customizeable and programmable facial coloring presets
- Toggle-able features
- Color pickers for features

### Misc
- "BACKGROUND" (transparent or filled)

### Face connections
- "FACE"
- "INNER_MOUTH"

- "LEFT_EYEBROW"
- "RIGHT_EYEBROW"

- "LEFT_EYEWHITE"
- "RIGHT_EYEWHITE"
- "RIGHT_PUPIL"
- "LEFT_PUPIL"
- "LEFT_EYELID"
- "RIGHT_EYELID"
- "B_LEFT_EYELID"
- "B_RIGHT_EYELID"
- "U_TEETH"
- "B_TEETH"
- "TOP_LIP"
- "BOTTOM_LIP"
- "RIGHT_NOSE"
- "LEFT_NOSE"
- "RIGHT_EAR"
- "LEFT_EAR"

### Hand connections
- "HAND_PALM"
- "HAND_THUMB"
- "HAND_POINTER"
- "HAND_MIDDLE"
- "HAND_RING"
- "HAND_PINKY"
