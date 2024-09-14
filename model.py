'''
This file will contains all the method needed by the eyecursorinterface.py
'''
import cv2

def left_eyebrow(frame, landmarks, frame_w, frame_h):
    #left eyebrow movement action
    left_eye_brow = [landmarks[66], landmarks[69]]
    for landmark in left_eye_brow:
        x = int(landmark.x * frame_w)
        y = int(landmark.y * frame_h)
        cv2.circle(frame, (x, y), 3, (0, 255, 255))

    if (abs(left_eye_brow[0].y - left_eye_brow[1].y)) < 0.040:
        print("left eyebrow detected")
        #pyautogui.click()

def right_eyebrow(frame, landmarks, frame_w, frame_h):
    #right eyebrow movement action
    right_eye_brow = [landmarks[296], landmarks[299]]
    for landmark in right_eye_brow:
        x = int(landmark.x * frame_w)
        y = int(landmark.y * frame_h)
        cv2.circle(frame, (x, y), 3, (0, 255, 255))

    if (abs(right_eye_brow[0].y - right_eye_brow[1].y)) < 0.040:
        print("right eyebrow detected")
        #pyautogui.click()

def mouth_open(frame, landmarks, frame_w, frame_h):
    #mouth open action
    mouth = [landmarks[13], landmarks[14]]
    for landmark in mouth:
        x = int(landmark.x * frame_w)
        y = int(landmark.y * frame_h)
        cv2.circle(frame, (x, y), 3, (0, 255, 255))

    if (abs(mouth[0].y - mouth[1].y)) > 0.012:
        print("mouth open")
        #pyautogui.press('ctrl')
        #pyautogui.press('ctrl')

def right_wink(frame, landmarks, frame_w, frame_h):
    #detect right wink
    right = [landmarks[374], landmarks[386]]
    for landmark in right:
        x = int(landmark.x * frame_w)
        y = int(landmark.y * frame_h)
        cv2.circle(frame, (x, y), 3, (0, 255, 255))

    if (right[0].y - right[1].y) < 0.012:
        print("right wink")
        #pyautogui.click()

def left_wink(frame, landmarks, frame_w, frame_h):
    # Detect left wink (blinking)
    left = [landmarks[145], landmarks[159]]
    for landmark in left:
        x = int(landmark.x * frame_w)
        y = int(landmark.y * frame_h)
        cv2.circle(frame, (x, y), 3, (0, 255, 255))

    current_time = cv2.getTickCount() / cv2.getTickFrequency()
    if ((left[0].y - left[1].y) < 0.012):
        print("left wink")
        pyautogui.click()
