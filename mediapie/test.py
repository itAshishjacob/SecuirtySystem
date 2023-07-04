import face_recognition
import cv2
import numpy as np

video_capture = cv2.VideoCapture(0)

obama = face_recognition.load_image_file("obama.jpg")
obama_enc = face_recognition.face_encodings(obama)[0]

biden = face_recognition.load_image_file("biden.jpg")
biden_enc = obama_enc = face_recognition.face_encodings(biden)[0]

known_enc = [
obama_enc,
biden_enc

]

known_face = [
    obama,
    biden
]


for i in known_enc :
    print (i)