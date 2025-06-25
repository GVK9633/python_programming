import cv2
from tracker import *


cap = cv2.VideoCapture(r"/Users/gvijaykumarachary/Desktop/MyComputer/E-Drive/DataScience/Repos/python_programming/Class_Room_Doc/June-2025/June-25-2025-opencv-object-tracking/24th, 25th- object tracking, Color detectio/11. Object tracking/object_tracking/highway.mp4")

# Object detection from Stable camera
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)


while True:
    ret, frame = cap.read()
    
    mask = object_detector.apply(frame)
     
    
    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', mask)
    
    key = cv2.waitKey(30)
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()