import cv2
import dlib

class detection:

    def __init__(self):
        self.faceDetection = dlib.get_frontal_face_detector()
        self.PointDetection = dlib.shape_predictor("archives/shape_predictor_68_face_landmarks.dat")

    def printPoint(self, img, facePoint):
        for p in facePoint.parts():
            cv2.circle(img, (p.x, p.y), 2, (255, 0, 0), 2)

    def printNum(self, img, facePoint):
        for i, p in enumerate(facePoint.parts()):
            cv2.putText(img, str(i), (p.x, p.y), cv2.FONT_HERSHEY_COMPLEX_SMALL, .55, (255, 0, 0), 1)

    def printRectangle(self, img, face):
        l, t, r, b = (int(face.left()), int(face.top()), int(face.right()), int(face.bottom()))
        cv2.rectangle(img, (l, t), (r, b), (255, 0, 0), 2)

    def printRectangleWithName(self, img, face, name, minimumDistance):
        l, t, r, b = (int(face.left()), int(face.top()), int(face.right()), int(face.bottom()))
        cv2.rectangle(img, (l, t), (r, b), (255, 0, 0), 2)
        text = "{} {:.4f}".format(name, minimumDistance)
        cv2.putText(img, text, (r, t), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0))

    def countFace(self, faceDetection):
        countFace = len(faceDetection)
        return countFace

    def detection(self, img):
        uframe = cv2.UMat(img)
        gray = cv2.UMat(cv2.cvtColor(uframe, cv2.COLOR_BGR2GRAY))
        facesDetection = self.faceDetection(cv2.UMat.get(gray))
        return {'detection': facesDetection, 'gray': gray}

    def HOG_Rectangle(self, img):
        for face in self.detection(img)['detection']:
            self.printRectangle(img, face)

    def HOG_Point(self, img):
        for face in self.detection(img)['detection']:
            point = self.PointDetection(cv2.UMat.get(self.detection(img)['gray']), face)
            self.printPoint(img, point)

    def HOG_Num(self, img):
        for face in self.detection(img)['detection']:
            point = self.PointDetection(cv2.UMat.get(self.detection(img)['gray']), face)
            self.printNum(img, point)
