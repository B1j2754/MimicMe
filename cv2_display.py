# Import libraries for face detection
import cv2
import mediapipe as mp
import pygame as pg
import numpy as np
import tkinter as tk
import pyvirtualcam

# Pull in values from config
import config

features = []
radius = 1

# Define the feature updates function
def update_features_from_queue(q):
    try:
        if not q.empty():
            updated_features = q.get_nowait()  # Get the latest feature data from the queue
            return updated_features
    except:
        return False

def window_cv2(q):
        global features

        # Initialize Pygame for displaying avatar
        pg.init()

        # Update features if necessary
        temp_features = update_features_from_queue(q)
        if temp_features:
            features = temp_features

        # Initialize MediaPipe Meshes
        mp_face_mesh = mp.solutions.face_mesh
        face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, refine_landmarks=True, min_detection_confidence=0.5)

        mp_hands = mp.solutions.hands
        hand_detector = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5)

        # Initialize camera
        capture = cv2.VideoCapture(0)
        capture.set(cv2.CAP_PROP_BUFFERSIZE, 2)

        # Initialize fps for display
        FPS = 60

        # Set up mouse callback
        ret, frame = capture.read()

        show_points = False
        fill_frame = True

        stop = False

        # Capture frame-by-frame
        ret, frame = capture.read()
        if not ret:
            stop = True

        # Get frame dimensions
        h, w, _ = frame.shape

        # Set up the Pygame display
        screen = pg.display.set_mode((w, h))
        pg.display.set_caption("OpenCV Frame in Pygame")

        # Clock to control the frame rate
        clock = pg.time.Clock()

        with pyvirtualcam.Camera(width=w, height=h, fps=60) as cam:

            while not stop:
                # Update features if necessary
                temp_features = update_features_from_queue(q)
                if temp_features:
                    features = temp_features
                
                # Capture frame-by-frame
                ret, frame = capture.read()
                if not ret:
                    stop = True

                # Get frame dimensions
                h, w, _ = frame.shape

                # Convert frame to RGB as MediaPipe works with RGB images
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Create a black image
                blank_screen = np.zeros((h, w, 3), np.uint8)

                # Find background color
                for i in features:
                    if i[0] == "BACKGROUND":
                        # Fill the image with green color
                        blank_screen[:] = i[1]

                        fill_frame = True
                        break
                    else:
                        fill_frame = False
                
                # Perform face landmark detection
                results = face_mesh.process(rgb_frame)

                # Draw each facial feature
                if results.multi_face_landmarks:
                    radii = [5]
                    for face_landmarks in results.multi_face_landmarks:
                        if features:
                            for feature_name, color, points in features:
                                adjusted_points = []
                                
                                # Draw each point in the specified order
                                for idx in points:
                                    landmark = face_landmarks.landmark[idx]
                                    x, y = int(landmark.x * w), int(landmark.y * h)
                                    
                                    # Draw a small circle at each landmark point
                                    if show_points:
                                        cv2.circle(frame, (x, y), 2, (0, 0, 255), -1)
                                    adjusted_points.append((x, y))
                                
                                # Draw filled polygon for the shape
                                if adjusted_points: # Check if points exist
                                    if feature_name in ["RIGHT_PUPIL", "LEFT_PUPIL"]: # Check if points need to be processed as eyes
                                        try:
                                            # Draw a filled circle at each pupil point
                                            radius = abs(adjusted_points[0][0] - adjusted_points[1][0])
                                            radii.append(radius)
                                            cv2.circle(blank_screen if fill_frame else frame, adjusted_points[0], radius-2, color, -1)
                                            cv2.circle(blank_screen if fill_frame else frame, adjusted_points[0], radius-5, (0,0,0), -1)
                                        except:
                                            radius = -1 # Failed bc no eyes found

                                    elif feature_name == "U_TEETH": # Check if points need to be processed as teeth
                                        for i in range(7):
                                            i = 6 - i
                                            adjusted_points.append((adjusted_points[i][0],adjusted_points[i][1]+max(radii)/2))
                                        # Draw a filled polygon for the teeth shape
                                        cv2.fillPoly(blank_screen if fill_frame else frame, [np.array(adjusted_points, dtype=np.int32)], color)

                                    elif "LIP" in feature_name: # Check if points need to be processed as lips
                                        cv2.fillPoly(blank_screen if fill_frame else frame, [np.array(adjusted_points, dtype=np.int32)], color)
                                        cv2.polylines(blank_screen if fill_frame else frame, [np.array(adjusted_points, dtype=np.int32)], True, color, 2)

                                    elif feature_name == "BACKGROUND" or feature_name.startswith("HAND"): # Check if points are hand points or background
                                        continue

                                    else: # Process points normally
                                        cv2.fillPoly(blank_screen if fill_frame else frame, [np.array(adjusted_points, dtype=np.int32)], color)

                # Perform hand landmark detection
                hand_results = hand_detector.process(rgb_frame)

                # Draw each hand
                if hand_results.multi_hand_landmarks:
                    for hand_landmarks in hand_results.multi_hand_landmarks:
                        if features:
                            for feature_name, color, points in features:
                                if feature_name.startswith("HAND"):
                                    adjusted_points = []

                                    # Draw each point in the specified order
                                    for idx in points:
                                        landmark = hand_landmarks.landmark[idx]
                                        x, y = int(landmark.x * w), int(landmark.y * h)
                                        
                                        # Draw a small circle at each landmark point
                                        if show_points:
                                            cv2.circle(frame, (x, y), 2, (0, 0, 255), -1)
                                        adjusted_points.append((x, y))
                                    
                                    # Draw filled polygon for the shape
                                    if adjusted_points: # Check if points exist
                                        try:
                                            if feature_name == "HAND_PALM": # Fill in palm
                                                cv2.fillPoly(blank_screen if fill_frame else frame, [np.array(adjusted_points, dtype=np.int32)], color)
                                                cv2.polylines(blank_screen if fill_frame else frame, [np.array(adjusted_points, dtype=np.int32)], False, color, max(radii) * 2)
                                            else:
                                                cv2.polylines(blank_screen if fill_frame else frame, [np.array(adjusted_points, dtype=np.int32)], False, color, max(radii) * 2)
                                        except:
                                            pass
                                            print(f"Failed to draw '{feature_name}'")

                # Convert bgr frame to rgb frame and display it on the virtual display
                virtual_frame = blank_screen if fill_frame else frame
                virtual_frame = cv2.cvtColor(virtual_frame, cv2.COLOR_BGR2RGB)

                # Convert the frame to a Pygame surface
                frame_surface = pg.surfarray.make_surface(virtual_frame.transpose(1, 0, 2))  # Pygame expects (width, height) order

                # Display the frame in Pygame
                screen.blit(frame_surface, (0, 0))
                pg.display.flip()

                # Send the frame to the virtual display
                cam.send(virtual_frame)
                cam.sleep_until_next_frame()

                # Check for Pygame events (e.g., window close)
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        stop = True

                # Cap the frame rate
                clock.tick(FPS)

            # Release capture and close window
            capture.release()
            cv2.destroyAllWindows()
            return "CV2 - Done!"