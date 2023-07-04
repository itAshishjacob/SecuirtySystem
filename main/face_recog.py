import face_recognition
import cv2
import numpy as np

video_capture = cv2.VideoCapture(0)

obama = face_recognition.load_image_file("obama.jpg")
obama_enc = face_recognition.face_encodings(obama)[0]

biden = face_recognition.load_image_file("biden.jpg")
biden_enc = obama_enc = face_recognition.face_encodings(biden)[0]

ashish = face_recognition.load_image_file("ashish.jpg")
ashish_enc = face_recognition.face_encodings(ashish)[0]

known_enc = [
obama_enc,
biden_enc,
ashish_enc

]

known_face = [
    "obama",
    "biden",
    'ashish'
]

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True :
    ret, frame = video_capture.read()

    if process_this_frame:

        small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)

        rgb_small_frame = small_frame[:,:,::-1]

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)\

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_enc,face_encoding)
            name = 'unknown'

            face_distances = face_recognition.face_distance(known_enc,face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    for (top, right, bottom, left),name in zip(face_locations,face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        
        cv2.rectangle(frame, (left,top),(right,bottom),(0,0,255),2)
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(frame,name,(left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()

