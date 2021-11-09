import cv2


class FaceAdjuster():
    def __init__(self, image, lms):
        self.img = image
        self.lms = lms

    def alignEyes(self):
        return True

    # The 2 paramiters lms are the 2 points of the face that will
    # be used to center the face and align it
    def alignFace(self, lmsUp, lmsDown):
        return True

    def getImage(self):
        return self.img
