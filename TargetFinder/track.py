#Developed by : Eugene Frazier
#Project : C.A.T.S_V1 (Computer Assist Target System)
#Last Updated :6/8/2017

import cv2
import logging as log
import datetime as dt
from time import sleep
import numpy as np



### define PARAMETERS####
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
log.basicConfig(filename='webcam.log',level=log.INFO)
font = cv2.FONT_HERSHEY_SIMPLEX

#Markers#
cross = [cv2.MARKER_CROSS]
diamond = [cv2.MARKER_DIAMOND]
square = [cv2.MARKER_SQUARE]

video_capture = cv2.VideoCapture(1)
anterior = 0

#### START FUNCTIONS#####
while True:
    if not video_capture.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass

    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 0), 2)

        for mt in diamond:  

           
            if  32*mt < x < 100*mt and 11*mt < y < 80*mt :
                words = "Locking" 

                a=0
                b=255
                c=0
                d=0
                e=255

                if  65*mt < x < 80*mt and 40*mt < y < 60*mt :
                    
                    words = "Target Lock"
                    a=255
                    b=0
                    c=0
                    d=0
                    e=255

            else :
                words = "Missed"
                a=0
                b=255
                c=0
                d=255
                e=0

        m1 = w//2
        m2 = h//2

        frame = cv2.drawMarker(frame, (m1+x,m2+y), (0,255,0),markerType=mt, markerSize=50, thickness=2, line_type=cv2.LINE_AA)
        print (words)
        cv2.putText(frame,words,(190,50), font, 1,(240,100,200),2,cv2.LINE_AA)

        for mt in cross:  
            frame = cv2.drawMarker(frame, (300,240), (0,a,b),markerType=mt, markerSize=100, thickness=2, line_type=cv2.LINE_AA)

        for mt in square:  
            frame = cv2.drawMarker(frame, (300,240), (d,e,0),markerType=mt, markerSize=200, thickness=2, line_type=cv2.LINE_AA)


               
    # Display the resulting frame
    cv2.imshow('Target Finder', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
