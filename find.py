import cv2
import mediapipe as mp
import numpy as np
from indices import MESH_CONNECTIONS

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, refine_landmarks=True, min_detection_confidence=0.5)

# Initialize the camera
capture = cv2.VideoCapture(0)

# Define data for features to colorize
features = [("LEFT_EYEBROW", (150, 65, 0)), ("RIGHT_EYEBROW", (150, 65, 0))]
feature_indices = [(MESH_CONNECTIONS[item[0]],item[1]) for item in features]

# Define mouse callback for tracking mouse
mouse_x =  0
mouse_y = 0
mouse_down = False
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Mouse click at:", x, y)
        global mouse_x, mouse_y, mouse_down
        mouse_x, mouse_y, mouse_down = x, y, True

# Set the mouse callback function
ret, frame = capture.read()
cv2.imshow('MediaPipe Face Mesh Avatar', frame)
cv2.setMouseCallback("MediaPipe Face Mesh Avatar", mouse_callback)
color = (0, 65, 150)

build = []

while True:
    # Capture frame-by-frame
    ret, frame = capture.read()
    if not ret:
        break

    # Get frame dimensions
    h, w, _ = frame.shape

    # Convert the frame color to RGB as MediaPipe works with RGB images
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Perform face landmark detection
    results = face_mesh.process(rgb_frame)

    # Draw shape
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            adjusted_points = []
            
            # Use manually defined order for left or right eyebrow
            points = [55, 107, 66, 105, 63, 46, 53, 52, 65, 55, 107]

            # Collect and scale the eyebrow points according to specified order
            for idx, val in enumerate(face_landmarks.landmark):
            #for idx in points:
                landmark = face_landmarks.landmark[idx]
                x, y = int(landmark.x * w), int(landmark.y * h)
                cv2.circle(frame, (x,y), 2, color)
                adjusted_points.append((x, y))

                # Check if point was clicked
                dist = abs(mouse_x-x)+abs(mouse_y-y)
                if dist < 3 and mouse_down:
                    print(f"Feature {idx} was clicked!")
                    build.append(idx)
                    mouse_x, mouse_y = 0, 0
                    mouse_down = False
            
            # Draw filled polygon for the shape
            # if adjusted_points:
            #     cv2.polylines(frame, [np.array(adjusted_points, dtype=np.int32)], isClosed=True, color=color)

    # Display the frame with drawn eyebrows
    cv2.imshow('MediaPipe Face Mesh Avatar', frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the capture
capture.release()
cv2.destroyAllWindows()
print(build)