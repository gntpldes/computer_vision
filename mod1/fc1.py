
#Importing Libraries
import cv2

#Loading the Cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#Defining a fucntion that will perform the detections
def detect(grey, frame): 
    faces = face_cascade.detectMultiScale(grey, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (44, 62, 80), 2)
        roi_grey = grey[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_grey, 1.1, 3)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (211, 84, 0), 2)
        return frame
    
#Facial Recognition with Webcam
video_capture = cv2.VideoCapture(0)
while True: 
    _, frame = video_capture.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GREY)
    canvas = detect(grey, frame)
    cv2.imshow('Video', canvas)
    if cv2.waitKey(1) & OxFF == ord('q'): 
        break
video_capture.release()
cv2.destroyAllWindows()
