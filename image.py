from face_detection_HOG import detection
from face_recognizer import recognizer
import cv2

class image:

    def __init__(self, file):
        self.detection = detection()
        self.recognizer = recognizer()
        self.img = cv2.imread(file)

    def image(self):
        cv2.imshow("Detector HOG", self.img)
        cv2.waitKey(0)
        cv2.destroyWindow()

    def img_Rectangle(self):
        self.detection.HOG_Rectangle(self.img)
        self.image()

    def img_Point(self):
        self.detection.HOG_Point(self.img)
        self.image()

    def img_Num(self):
        self.detection.HOG_Num(self.img)
        self.image()

    def img_recognizer(self):
        self.recognizer.recognizer(self.img)
        self.image()