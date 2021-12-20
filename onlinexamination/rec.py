import face_recognition
import cv2
import numpy as np
import requests
known_face_encodings = [
    
]
known_face_names = [
    "Sathya Bama","Snekha"
]

vid = cv2.VideoCapture(0)
captured = False
image = face_recognition.load_image_file("photo.jpg")
image_encoding = face_recognition.face_encodings(image)[0]
known_face_encodings.append(image_encoding)
while(True):
    ret, frame = vid.read()
    if captured:

       
        if cv2.waitKey(1) & 0xFF == ord('c'):
            cv2.imwrite("photo.jpg",frame)
            image = face_recognition.load_image_file("photo.jpg")
            image_encoding = face_recognition.face_encodings(image)[0]
            known_face_encodings.append(image_encoding)
            captured = False
        cv2.imshow("frame",frame)
        continue
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"

        # If a match was found in known_face_encodings, just use the first one.
        # if True in matches:
        #     first_match_index = matches.index(True)
        #     name = known_face_names[first_match_index]

        # Or instead, use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        if name == "Unknown":  #known_face_names[0]:
            requests.get("http://127.0.0.1:8000")

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    face_locations = face_recognition.face_locations(image)
    cv2.imshow('frame', frame)
      

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()


