import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection()

pTime = 0
cTime = 0 

while True: 
    success , img = cap.read()

    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)
    print(results)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)),(10,70),(cv2.FONT_HERSHEY_DUPLEX),2,(0,0,225),3)
    
    cv2.imshow('image',img)
    cv2.waitKey(1)
