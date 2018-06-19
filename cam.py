from face_detection_HOG import detection
from face_recognizer import recognizer
import cv2
import sys

class cam():

    def __init__(self, capture):
        self.detection = detection()
        self.recognizer = recognizer()
        self.cap = cv2.VideoCapture(capture)

    def close(self):
        self.cap.release()
        cv2.destroyAllWindows()
        sys.exit(0)

    def cam_Rectangle(self):
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            self.detection.HOG_Rectangle(frame)
            cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xFF == 27:
                break
        self.close()

    def cam_Point(self):
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            self.detection.HOG_Point(frame)
            cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xFF == 27:
                break
        self.close()

    def cam_Num(self):
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            self.detection.HOG_Num(frame)
            cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xFF == 27:
                break
        self.close()

    def cam_recognizer(self):
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            self.recognizer.recognizer(frame)
            cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xFF == 27:
                break
        self.close()
