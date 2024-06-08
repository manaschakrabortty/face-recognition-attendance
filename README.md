Face Recognition Based Attendance System
This project implements an attendance tracking system using face recognition technology. It captures video input from a webcam, recognizes faces in real-time, 
and marks logs the attendance of known individuals in a CSV file with the current date and time.

Features:- 
  Real-time face recognition using the webcam.
  Attendance marking and timestamp recording for known individuals.
  CSV file generation for attendance records.
  Handles multiple known faces.
  Simple and intuitive interface using OpenCV.

Requirements
  Python 3.x
  OpenCV
  face_recognition
  numpy

Add known faces :-
  Add images of known individuals in the faces directory.
  Update the script to include the new faces.

Interaction:
  The system will open the webcam and start detecting faces.
  Detected known faces will be logged as present in a CSV file named with the current date.
  To stop the script, press the 'q' key.

How It Works:- 
  Load Known Faces: The system loads images of known individuals and encodes their faces using the face_recognition library.
  Capture Video: The system captures video from the webcam.
  Detect and Recognize Faces: For each frame captured from the video, the system detects faces and compares them with the known faces.
  Log Attendance: If a face is recognized, the person's name and the current time are logged into a CSV file named with the current date.

  Code Explanation
  The main script attendance.py performs the following steps:
    Load known faces: Loads images of known individuals and generates their face encodings.
    Video capture: Captures video from the webcam.
    Face recognition: Resizes the video frame for faster processing, converts it to RGB, and detects face locations and encodings.
    Match faces: Compares detected face encodings with known face encodings and identifies the best match.
    Mark attendance: If a known face is recognized, it displays the name on the screen and writes the attendance to a CSV file with a timestamp.
    Exit: Press q to quit the application and close the CSV file.

Contributing
  Feel free to contribute to this project and If you have any suggestions or improvements, 
  please submit a pull request or open an issue.

  THANK YOU
