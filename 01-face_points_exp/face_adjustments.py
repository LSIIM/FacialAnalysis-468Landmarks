import cv2
import numpy as np


class FaceAdjuster():
    def __init__(self, image, lms):
        self._img = image
        self._lms = lms

    def alignEyes(self):
        top, left, bottom, right = self._find_face_border()
        eyes_cent_img = []
        print(top, left, bottom, right)
        if top < 0:
            top = 0
        if left < 0:
            left = 0
        for j in range(top, bottom):
            row = []
            if(j >= self._img.shape[0]):
                continue
            for i in range(left, right):
                if(i >= self._img.shape[1]):
                    continue
                row.append(self._img[j][i])
            eyes_cent_img.append(row)
        eyes_cent_img = np.array(eyes_cent_img)
        return eyes_cent_img

    # The 2 paramiters lms are the 2 points of the face that will
    # be used to center the face and align it
    def alignFace(self, lmsUp, lmsDown):
        return True

    # private mathods
# ------------------------------------------------------

    def _getImage(self):
        return self._img

    def _face_bottom(self):
        highest = None
        for lm in self._lms:
            if highest == None:
                highest = lm[1]
                continue
            if lm[1] > highest:
                highest = lm[1]
        return highest

    def _face_top(self):
        lowest = None
        for lm in self._lms:
            if lowest == None:
                lowest = lm[1]
                continue
            if lm[1] < lowest:
                lowest = lm[1]
        return lowest

    def _face_left(self):
        lowest = None
        for lm in self._lms:
            if lowest == None:
                lowest = lm[0]
                continue
            if lm[0] < lowest:
                lowest = lm[0]
        return lowest

    def _face_right(self):
        highest = None
        for lm in self._lms:
            if highest == None:
                highest = lm[0]
                continue
            if lm[0] > highest:
                highest = lm[0]
        return highest

    # https://github.com/ManuelTS/augmentedFaceMeshIndices/blob/master/Left_Eye_shading.jpg
    def _find_face_border(self):
        return self._face_top(), self._face_left(), self._face_bottom(), self._face_right()
