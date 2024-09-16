import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import model
import calabration

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

# Initialize smoothing variables
alpha = 0.5  # Smoothing factor (between 0 and 1)
prev_x, prev_y = 0.5, 0.5  # Initial previous positions (normalized)
pyautogui.PAUSE = 0.01
pyautogui.FAILSAFE = False

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

#check if text dictation is open for speech to text
isOpen = False
#boolean to control the mouse down with long left eye hold
isMouseDown = False
while True:
    ret, frame = cam.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    #frame.flags.writeable = False
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks

    # Indices for the eye landmarks (including irises) and Mouth
    #left_eye_landmarks = [33, 133, 144, 145, 153, 154, 155, 159, 160, 161, 163, 173]
    left_eye_upper_landmarks = np.array([33,246,161,160,159,158,157,173,133]) 
    left_eye_lower_landmarks = np.array([33,7, 163,144,145,153,154,155,133])

    #right_eye_landmarks = [362, 382, 383, 384, 385, 386, 387, 388, 390, 398]
    right_eye_upper_landmarks = [362,398,384,385,386,387,388,466,263]
    right_eye_lower_landmarks = [362,382,381,380,374,373,390,249,263]
    left_iris_landmarks = [468, 469, 470, 471, 472]
    right_iris_landmarks = [473, 474, 475, 476, 477]
    MOUTH_LANDMARKS = [61, 185, 40, 39, 37, 0, 267, 269, 270, 409, 291, 375, 321, 405, 314, 17, 84, 181, 91, 146, 61]

    frame_h, frame_w, _ = frame.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark

        # Calculate average position of the iris
        avg_x = sum(landmarks[idx].x for idx in right_iris_landmarks) / len(right_iris_landmarks)
        avg_y = sum(landmarks[idx].y for idx in right_iris_landmarks) / len(right_iris_landmarks)
            
        # Move the mouse cursor based on smoothed eye positions
        move_mouse(screen_w, avg_x, screen_h, avg_y)

        # Draw landmarks for the iris
        for idx in left_iris_landmarks:
            x = int(landmarks[idx].x * frame_w)
            y = int(landmarks[idx].y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
    
#        for idx in MOUTH_LANDMARKS:
#            x = int(landmarks[idx].x * frame_w)
#            y = int(landmarks[idx].y * frame_h)
#            cv2.circle(frame, (x, y), 3, (0, 255, 0))

        #pupil up and down for pressEnter
        model.pressEnter(frame, landmarks, frame_w, frame_h)
#
        #pupil movement for back and forth
        model.back_n_forth(frame, landmarks, frame_w, frame_h)

        #eyerbow for scrolling movement
        model.eyebrows(frame, landmarks, frame_w, frame_h)

        #left eyebrow movement
        #model.left_eyebrow(frame,landmarks, frame_w, frame_h)
        #right eyebrow movement
        #model.right_eyebrow(frame, landmarks, frame_w, frame_h)

        #mouth open is action for speech to text
        model.mouth_open(frame, landmarks, frame_w, frame_h, isOpen)

        #right wink for mouse right click
        model.right_wink(frame, landmarks, frame_w,frame_h)

        # Detect left wink (blinking)
        # model.left_wink(frame, landmarks,frame_w,frame_h)

        # Detect Smile for scrolling movement
        model.smile(frame, landmarks,frame_w,frame_h)

        #Left wink ovepration is still magaged here due to time interval association

        #left eye 
        left_eye_upper_landmarks = np.array([landmarks[idx].y for idx in left_eye_upper_landmarks])
        left_eye_lower_landmarks = np.array([landmarks[idx].y for idx in left_eye_lower_landmarks])
        res_left_eye = np.subtract(left_eye_upper_landmarks,left_eye_lower_landmarks)

        #right eye
        right_eye_upper_landmarks = np.array([landmarks[idx].y for idx in right_eye_upper_landmarks])
        right_eye_lower_landmarks = np.array([landmarks[idx].y for idx in right_eye_lower_landmarks])
        res_right_eye = np.subtract(right_eye_upper_landmarks,right_eye_lower_landmarks)

        current_time = cv2.getTickCount() / cv2.getTickFrequency()
        print("left: ",abs(np.sum(res_left_eye)) )
        print("right:",abs(np.sum(res_right_eye)))
        if abs(np.sum(res_left_eye)) < 0.020 and abs(np.sum(res_right_eye)) > 0.015:
            #if current_time - last_click_time >= click_interval:
            print("wink")
            pyautogui.click()
            #last_click_time = current_time  # Update last click time
#            else:
#                if isMouseDown:
#                    pyautogui.mouseUp(button = 'left')
#                    isMouseDown = False
#                else:
#                    print("long wink")
#                    pyautogui.mouseDown(button='left')
#                    isMouseDown = True

#        left = [landmarks[145], landmarks[159]]
#        right = [landmarks[374], landmarks[386]]
#        for landmark in left:
#            x = int(landmark.x * frame_w)
#            y = int(landmark.y * frame_h)
#            cv2.circle(frame, (x, y), 3, (0, 255, 255))

#        current_time = cv2.getTickCount() / cv2.getTickFrequency()
#        if (abs(left[0].y - left[1].y) < 0.012) and (abs(right[0].y - right[1].y) > 0.015):
#            x = 0
#            if current_time - last_click_time >= click_interval:
#                print("wink")
#                pyautogui.click()
#                last_click_time = current_time  # Update last click time
#            else:
#                print("long wink")
#                pyautogui.mouseDown(button='left')
            

    #cv2.imshow('Eye Controlled Mouse', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
