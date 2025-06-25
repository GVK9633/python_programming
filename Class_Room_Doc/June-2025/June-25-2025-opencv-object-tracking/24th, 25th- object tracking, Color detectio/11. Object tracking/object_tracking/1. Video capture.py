import cv2
from tracker import* #tracking contain 8 tracking algo

# https://pyimagesearch.com/2018/07/30/opencv-object-tracking/


cap = cv2.VideoCapture(r"C:\Users\A3MAX SOFTWARE TECH\Desktop\WORK\2. DATASCIENCE PROJECT\11. Object tracking\object_tracking\highway.mp4")

while True:
    ret, frame = cap.read()
    
    cv2.imshow('Frame', frame)
    
    key = cv2.waitKey(30)
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()