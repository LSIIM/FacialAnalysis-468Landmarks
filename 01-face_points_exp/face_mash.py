import cv2
import mediapipe
import numpy as np


class FaceMashDetector():
    def __init__(self,
                 image=None,
                 staticImageMode=False,
                 maxNumFaces=1,
                 minDetectionConfidence=0.8,
                 minTrackingConfidence=0.5):

        self._staticImageMode = bool(staticImageMode)
        self._maxNumFaces = int(maxNumFaces)
        self._minDetectionConfidence = float(minDetectionConfidence)
        self._minTrackingConfidence = float(minTrackingConfidence)

        self._mpDraw = mp.solutions.drawing_utils
        self._mpFaceMesh = mp.solutions.face_mesh

        self._faceMesh = self._mpFaceMesh.FaceMesh(max_num_faces=self._maxNumFaces,
                                                   min_detection_confidence=self._minDetectionConfidence,
                                                   static_image_mode=self._staticImageMode,
                                                   min_tracking_confidence=self._minTrackingConfidence)

        self._drawSpec = self._mpDraw.DrawingSpec(thickness=1, circle_radius=2)
        self._lms = []
        self._img = image

    def findFaceMesh(self):
        imgRGB = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        results = self._faceMesh.process(imgRGB)
        self._lms = []
        if results.multi_face_landmarks:
            for faceLms in results.multi_face_landmarks:
                face = []
                for lm in faceLms.landmark:
                    ih, iw, ic = self.img.shape
                    x, y = int(lm.x*iw), int(lm.y*ih)
                    face.append((x, y))
                self._lms.append(face)
            return True
        else:
            return False

    def getLms(self):
        return self._lms
