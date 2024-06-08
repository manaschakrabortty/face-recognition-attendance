# pip install cmake
# pip install face_recognition
# pip install opencv-python
# pip install numpy


import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)

#load known faces
manas_image = face_recognition.load_image_file("faces/manas.jpeg")
manas_encoding = face_recognition.face_encodings(manas_image)[0]

purbasa_image = face_recognition.load_image_file("faces/purbasa.jpeg")
purbasa_encoding = face_recognition.face_encodings(purbasa_image)[0]

manasi_images = face_recognition.load_image_file("faces/manasi.jpeg")
manasi_encoding = face_recognition.face_encodings(manasi_images)[0]

biswajit_image = face_recognition.load_image_file("faces/biwajit.jpg")
biwajit_encoding = face_recognition.face_encodings(biswajit_image)[0]

known_face_encodings = [manas_encoding,purbasa_encoding,manasi_encoding,biwajit_encoding]
known_face_names = ["Manas","Purbasa","Manasi","Biswajit"]

#list of expected students
students = known_face_names .copy()

face_locations=[]
face_encodings =[]

# Get the current date and time
now = datetime.now()
current_date = now.strftime("%d-%m-%Y")

f = open(f"{current_date}.csv", "w+", newline="")
lnwrite = csv.writer(f)

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame,(0, 0), fx = 0.25, fy=0.25)
    rgb_small_frame =cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
    
    #RECOGNIZE FACES
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)


    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings,face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)

        best_match_index = np.argmin(face_distance)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]
        else:
            name = None  # Initialize name as None if there is no match

        # Add the text if a person is present
        if name in known_face_names:
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottomleftcornerofText = (10, 100)
            fontScale= 1.5
            fontColor = (255, 0, 0)
            thickness = 3
            lineType = 2
            # cv2.putText(frame, name + "Present",bottomleftcornerofText,fontScale,fontColor,thickness, lineType)
            cv2.putText(frame, name + " Present", bottomleftcornerofText, font, fontScale, fontColor, thickness, lineType)



            if name in students:
                students.remove(name)
                current_time = datetime.now().strftime("%H:%M:%S")
                lnwrite.writerow([name,current_time])

        cv2.imshow("Attendance" , frame)
        if cv2.waitKey(1) & 0xFF ==ord("q"):
            break


video_capture.release()
cv2.destroyAllWindows()
f.close()




