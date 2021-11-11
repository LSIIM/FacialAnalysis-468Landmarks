import cv2
import numpy as np
from numpy.core.fromnumeric import resize
from scipy import ndimage
import math
pi = 3.14159265359


class FaceAdjuster():
    def __init__(self, image, lms):
        self._img = image
        self._lms = lms

    def alignEyes(self):

        xR, yR = self._lms[362]
        xL, yL = self._lms[133]
        row, col = self._img.shape[:2]
        angle = math.atan2(
            (yR-yL), (xR-xL))
        rotated = ndimage.rotate(self._img, angle*180/pi, reshape=False)

        print((yR-yL)/(xR-xL))  # tangente
        print(math.atan2((yR-yL), (xR-xL)))  # radianos
        print(math.atan2((yR-yL), (xR-xL))*180/pi)  # graus
        for i, lm in enumerate(self._lms):
            dy = ((row/2)-(lm[1]))
            dx = (-(col/2)+lm[0])

            #print("shift: ", angle)
            old_angle = math.atan2(
                dy, dx)

            #print("actual: ", old_angle)
            #print(self._lms[i], (dx, dy))

            r = math.sqrt(dy*dy + dx*dx)
            newposX = r * math.cos((old_angle+angle))
            newposY = r * math.sin((old_angle+angle))

            self._lms[i] = [int(newposX+(col/2)), int(-newposY + (row/2))]

        return rotated

    def getLms(self):
        return self._lms
    # The 2 paramiters lms are the 2 points of the face that will
    # be used to center the face and align it

    def alignFace(self):
        # deixa o rosto sempre na mesma posição
        rows, cols = self._img.shape[:2]
        pos = self._lms[10]
        distX = int(cols/2)-int(pos[0])
        distY = 25-int(pos[1])
        M = np.float32(
            [[1, 0, distX], [0, 1, distY]])
        dst = cv2.warpAffine(self._img, M, (cols, rows))

        for i, lm in enumerate(self._lms):
            self._lms[i] = [self._lms[i][0]+distX, self._lms[i][1]+distY]

        return dst

    def faceCrop(self):
        rows, cols = self._img.shape[:2]
        top, left, bottom, right = self._find_face_border()
        cent_img = []
        prop = 500/rows
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
            cent_img.append(row)
        cent_img = np.array(cent_img)
        cent_img = self._image_resize(cent_img, height=500)
        for i, lm in enumerate(self._lms):
            self._lms[i] = [int((self._lms[i][0]-top)/(cols*prop)),
                            int((self._lms[i][1]-left)/(rows*prop))]
        return cent_img
    # private mathods
# ------------------------------------------------------

    def _image_resize(self, img, width=None, height=None, inter=cv2.INTER_AREA):
        dim = None
        (h, w, _) = img.shape

        if width is None and height is None:
            return img

        if width is None:
            r = height / float(h)
            dim = (int(w * r), height)

        else:
            r = width / float(w)
            dim = (width, int(h * r))

        resized = cv2.resize(img, dim, interpolation=inter)
        return resized

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
        margin = 60
        return self._face_top()-margin, self._face_left()-margin, self._face_bottom()+margin, self._face_right()+margin

    def _find_l_eye_border(self):
        # top,left,bottom,right
        return self._lms[27][1], self._lms[130][0], self._lms[23][1], self._lms[133][0]

    def _find_r_eye_border(self):
        # top,left,bottom,right
        return self._lms[386][1], self._lms[362][0], self._lms[253][1], self._lms[263][0]
