import cv2
import mediapipe as mp
import pyautogui
import numpy as np

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

# Initialize smoothing variables
alpha = 0.5  # Smoothing factor (between 0 and 1)
prev_x, prev_y = 0.5, 0.5  # Initial previous positions (normalized)

# Variable to manage the timing of clicks
last_click_time = 0
click_interval = 0.5  # Minimum interval between clicks in seconds

def move_mouse(screen_width, x, screen_height, y):
    global prev_x, prev_y
    
    # Smooth out the eye position using exponential moving average
    x = alpha * x + (1 - alpha) * prev_x
    y = alpha * y + (1 - alpha) * prev_y
    
    # Update previous positions
    prev_x, prev_y = x, y

    # Convert normalized coordinates to screen coordinates
    screen_x = x * screen_width
    screen_y = y * screen_height
    screen_x = (5 * (screen_x - screen_width / 2) + screen_width / 2)
    screen_y = (5 * (screen_y - screen_height / 2) + screen_height / 2)
    
    # Apply boundary constraints
    screen_x = np.clip(screen_x, 0, screen_width - 1)
    screen_y = np.clip(screen_y, 0, screen_height - 1)
    
    pyautogui.moveTo(screen_x, screen_y)

while True:
    ret, frame = cam.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks

    # Indices for the eye landmarks (including irises)
    left_eye_landmarks = [33, 133, 144, 145, 153, 154, 155, 159, 160, 161, 163, 173]
    right_eye_landmarks = [362, 382, 383, 384, 385, 386, 387, 388, 390, 398]
    left_iris_landmarks = [468, 469, 470, 471]
    right_iris_landmarks = [473, 474, 475, 476]

    frame_h, frame_w, _ = frame.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark

        # Calculate average position of the iris
        avg_x = sum(landmarks[idx].x for idx in right_iris_landmarks) / len(right_iris_landmarks)
        avg_y = sum(landmarks[idx].y for idx in right_iris_landmarks) / len(right_iris_landmarks)

        # Move the mouse cursor based on smoothed eye positions
        move_mouse(screen_w, avg_x, screen_h, avg_y)

        # Draw landmarks for the iris
        for idx in right_iris_landmarks:
            x = int(landmarks[idx].x * frame_w)
            y = int(landmarks[idx].y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))

        #mouth open is action
        mouth = [landmarks[13], landmarks[14]]
        for landmark in mouth:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))

        if (abs(mouth[0].y - mouth[1].y)) > 0.012:
            print("mouth open")
            pyautogui.click()

        #detect right wink
        right = [landmarks[374], landmarks[386]]
        for landmark in right:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))

        if (right[0].y - right[1].y) < 0.012:
            print("right wink")
            pyautogui.click()

        # Detect left wink (blinking)
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))

        current_time = cv2.getTickCount() / cv2.getTickFrequency()
        if (left[0].y - left[1].y) < 0.012:
            print("wink")
            pyautogui.click()
#            if current_time - last_click_time >= click_interval:
#                print("wink")
#                pyautogui.click()
#                last_click_time = current_time  # Update last click time

    # cv2.imshow('Eye Controlled Mouse', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
