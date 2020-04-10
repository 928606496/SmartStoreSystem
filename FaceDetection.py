import cv2 as cv
import os
from PIL import ImageGrab


class FaceDetection():
    def __init__(self):
        self.path = os.getcwd()+'/Detection.png'
        self.classifier = os.getcwd()+'/haarcascade_frontalface_default.xml'

    def detect(self):
        #Get the picture
        image = cv.imread(self.path)

        #Grayscale transformation
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

        #Get faces recognition train data
        face_casacade = cv.CascadeClassifier(self.classifier)

        #Detece the face in the picture
        faces = face_casacade.detectMultiScale(image)

        # Set rectangle around the face in target picture
        color = (0,0,255)
        strokeWeight = 1
        num = 1
        for x, y, width, height in faces:
            cv.rectangle(image, (x, y), (x + width, y + height), color, strokeWeight)
            grabScale = (x -20,y -20, x + width + 20,y + height + 20)
            im = ImageGrab.grab(grabScale)
            faces_path = ("./GrabedFaces/GrabedFace"+str(num)+".png")
            im.save(faces_path)
            num += 1
        # Save the result
        # cv.imwrite("FaceDetectionResult.jpg",image)
        return len(faces)
