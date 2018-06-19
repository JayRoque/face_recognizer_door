import os
import glob
import _pickle as cPickle
import dlib
import cv2
import numpy as np

class trainning:

    def __init__(self, file):
        self.faceDetection = dlib.get_frontal_face_detector()
        self.PointDetection = dlib.shape_predictor("archives/shape_predictor_68_face_landmarks.dat")
        self.faceRecognizer = dlib.face_recognition_model_v1("archives/dlib_face_recognition_resnet_model_v1.dat")
        self.index = {}
        self.idx = 0
        self.faceDescriptors = None
        self.file = file

    def train(self):
        #percorre a pasta de treinamento
        for archives in glob.glob(os.path.join(self.file, "*.png")): #pasta com as imagem de trainamento "img/photos"
            img = cv2.imread(archives)
            facesDetection = self.faceDetection(img, 1)
            numFaces = len(facesDetection)

            #vericação se a mais de uma face para o treinamento
            if numFaces > 1:
                print("Há mais de uma face na imagem {}".format(archives))
                exit(0)
            elif numFaces < 1:
                print("Nenhuma face na imagem {}".format(archives))
                exit(0)

            for face in facesDetection:
                facePoint = self.PointDetection(img, face)
                faceDescriptor = self.faceRecognizer.compute_face_descriptor(img, facePoint)
                listFaceDescriptor = [df for df in faceDescriptor]
                npArrayFaceDescriptor = np.asarray(listFaceDescriptor, dtype=np.float64)
                npArrayFaceDescriptor = npArrayFaceDescriptor[np.newaxis, :]

                if self.faceDescriptors is None:
                    self.faceDescriptors = npArrayFaceDescriptor
                else:
                    self.faceDescriptors = np.concatenate((self.faceDescriptors, npArrayFaceDescriptor), axis=0)

                self.index[self.idx] = archives
                self.idx += 1

        np.save("img/archives/descritores.npy", self.faceDescriptors)
        with open("img/archives/indice.pickle", "wb") as f:
            cPickle.dump(self.index, f)