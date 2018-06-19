import os
from face_detection_HOG import detection
import dlib
import cv2
import numpy as np
from bot_telegram import bot
from arduino_conection import arduino as con


class recognizer():

    def __init__(self):
        self.con = con()
        self.bot = bot()
        self.detection = detection()
        self.faceRecognizer = dlib.face_recognition_model_v1("archives/dlib_face_recognition_resnet_model_v1.dat")
        self.indexes = np.load("img/archives/indice.pickle")
        self.faceDescriptors = np.load("img/archives/descritores.npy")
        self.linear = 0.5
        self.aux = 0

    def KNN(self, img, npArrayFaceDescriptor):
        distances = np.linalg.norm(npArrayFaceDescriptor - self.faceDescriptors, axis=1)
        minimum = np.argmin(distances)
        minimumDistance = distances[minimum]

        if minimumDistance <= self.linear:
            name = os.path.split(self.indexes[minimum])[1].split(".")[0]

            if self.aux != name:
                self.bot.msg("Olá {}, seja bem vindo !!!".format(name))
                self.aux = name
            self.con.led('1')

        else:
            name = "desconhecido(a)"
            self.con.led('0')

            if self.aux != name:
                self.bot.msg("Tem uma pessoa {} na sua porta !!!".format(name))
                capture = cv2.imwrite("faces/unklock.png", img)
                self.bot.img("faces/unklock.png")
                self.aux = name
        return {'name': name, 'distance': minimumDistance}

    def recognizer(self, img):

        countFace = self.detection.countFace(self.detection.detection(img)['detection'])
        print("Faces Detectadas: ", countFace)

        if countFace == 0:
            self.aux = ""

        for face in self.detection.detection(img)['detection']:
            facesPoint = self.detection.PointDetection(cv2.UMat.get(self.detection.detection(img)['gray']), face)
            faceDescriptor = np.array(self.faceRecognizer.compute_face_descriptor(img, facesPoint))

            listFaceDescriptor = [fd for fd in faceDescriptor]
            npArrayFaceDescriptor = np.asarray(listFaceDescriptor, dtype=np.float)
            npArrayFaceDescriptor = npArrayFaceDescriptor[np.newaxis, :]

            self.KNN(img, npArrayFaceDescriptor)

            self.detection.printRectangleWithName(img, face, self.KNN(img, npArrayFaceDescriptor)['name'], self.KNN(img, npArrayFaceDescriptor)['distance'])
