import cv2
from tracker import * #tracking contain 8 tracking algo

# https://pyimagesearch.com/2018/07/30/opencv-object-tracking/


cap = cv2.VideoCapture(r"/Users/gvijaykumarachary/Desktop/MyComputer/E-Drive/DataScience/Repos/python_programming/Class_Room_Doc/June-2025/June-25-2025-opencv-object-tracking/24th, 25th- object tracking, Color detectio/11. Object tracking/object_tracking/highway.mp4")

while True:
    ret, frame = cap.read()
    
    cv2.imshow('Frame', frame)
    
    key = cv2.waitKey(30)
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()