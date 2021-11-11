from face_adjustments import FaceAdjuster
from face_mash import FaceMashDetector
import os
import cv2
import numpy as np
import math
DATASET_PATH = r"D:\OneDrive - Etec Centro Paula Souza\Academico\UFSC\MIGMA\migma_dataset"


def fixFacePosition(image):
    print(image.shape)
    print((int(image.shape[0]/2), int(image.shape[1]/2)))
    image = cv2.resize(image, (int(image.shape[1]/2), int(image.shape[0]/2)))
    cv2.imshow("img", image)
    cv2.waitKey(0)
    meshed = FaceMashDetector(image=image)
    if(not meshed.findFaceMesh()):
        print("No faces")
        return None

    lms = meshed.getLms()[0]

    # -------- Teste -----------------
    # cv2.imshow("orig", image)
    di = image.copy()
    print("Eyes")
    print(int(1000*math.cos(0)), int(1000*math.sin(90*3.14159265359/180)))
    cv2.putText(di, ".", (int(1000*math.cos(0)), int(1000*math.sin(90*3.14/180))), cv2.FONT_HERSHEY_PLAIN,
                8, (255, 255, 0), 5)
    for i in range(len(lms)):
        cv2.putText(di, ".", lms[i], cv2.FONT_HERSHEY_PLAIN,
                    0.8, (0, 255, 0), 1)

    cv2.imshow("img", di)
    cv2.waitKey(0)
    # ---------------------------------

    adjuster1 = FaceAdjuster(image.copy(), lms.copy())
    eyes_cent_img = adjuster1.alignEyes()

    nlms = adjuster1._lms
    print("------------------------------------------------------------")
    # -------- Teste -----------------
    # cv2.imshow("orig", image)
    print("Eyes")

    for i in range(len(lms)):
        cv2.putText(eyes_cent_img, ".", nlms[i], cv2.FONT_HERSHEY_PLAIN,
                    0.8, (255, 0, 0), 1)

    cv2.imshow("img", eyes_cent_img)
    cv2.waitKey(0)
    # ---------------------------------

    adjuster2 = FaceAdjuster(eyes_cent_img.copy(), nlms.copy())
    face_fix_img = adjuster2.alignFace()

    nlms = adjuster2._lms
    print("------------------------------------------------------------")
    # -------- Teste -----------------
    # cv2.imshow("orig", image)
    print("Eyes")

    for i in range(len(lms)):
        cv2.putText(face_fix_img, ".", nlms[i], cv2.FONT_HERSHEY_PLAIN,
                    0.8, (255, 0, 0), 1)

    cv2.imshow("img", face_fix_img)
    cv2.waitKey(0)
    # ---------------------------------

    adjuster3 = FaceAdjuster(face_fix_img.copy(), nlms.copy())
    crop_img = adjuster3.faceCrop()

    nlms = adjuster3._lms
    print("------------------------------------------------------------")
    # -------- Teste -----------------
    # cv2.imshow("orig", image)
    print("Eyes")

    for i in range(len(lms)):
        cv2.putText(crop_img, ".", nlms[i], cv2.FONT_HERSHEY_PLAIN,
                    0.8, (255, 0, 0), 1)

    cv2.imshow("img", crop_img)
    cv2.waitKey(0)
    # ---------------------------------

    return eyes_cent_img


def analyseFace(image, name):
    fixed_image = fixFacePosition(image)

    print("fim")
    return True


if __name__ == "__main__":
    print("Começando analise")
    test_path = r"D:\OneDrive - Etec Centro Paula Souza\Academico\UFSC\MIGMA\migma_dataset\01\00\04435"
    fotos = os.listdir(test_path)
    path = test_path + "/"+fotos[1]

    img = cv2.imread(path)
    analyseFace(img, fotos[1])
    '''
    expressions = os.listdir(DATASET_PATH)
    for exp in expressions:
        types = os.listdir(DATASET_PATH + "/"+exp)
        for tp in types:
            users = os.listdir(DATASET_PATH + "/"+exp+"/"+tp)
            print(users)
    '''
