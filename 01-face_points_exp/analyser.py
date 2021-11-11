from face_adjustments import FaceAdjuster
from face_mash import FaceMashDetector
import os
import cv2
import numpy as np
import math
DATASET_PATH = r"D:\OneDrive - Etec Centro Paula Souza\Academico\UFSC\MIGMA\migma_dataset"


def fixFacePosition(image):
    # print(image.shape)
    #print((int(image.shape[0]/2), int(image.shape[1]/2)))
    row, col = image.shape[:2]
    img_new_width = 900
    rt = img_new_width/col
    image = cv2.resize(image, (img_new_width, int(row*rt)))

    meshed = FaceMashDetector(image=image)
    if(not meshed.findFaceMesh()):
        print("No faces")
        cv2.imshow("Erro", image)
        cv2.waitKey(0)
        return None

    lms = meshed.getLms()[0]

    # --------------------------------------------------------------------------
    adjuster = FaceAdjuster(image.copy(), lms.copy())
    eyes_cent_img = adjuster.alignEyes()
    face_fix_img = adjuster.alignFace()
    crop_img = adjuster.faceCrop()
    face_fix_img2 = adjuster.alignFace()
    border_img = adjuster.fixImageSizeWitBorders()
    nlms = adjuster._lms
    # print("------------------------------------------------------------")
    # -------- Teste -----------------
    # cv2.imshow("orig", image)
    di = border_img.copy()
    # print("Crop")
    # print(nlms[10])
    # print(nlms[152][1]-nlms[10][1])
    for i in range(len(nlms)):
        cv2.putText(di, ".", nlms[i], cv2.FONT_HERSHEY_PLAIN,
                    0.8, (0, 255, 0), 1)

    cv2.imshow("img", di)
    cv2.waitKey(1)
    # ---------------------------------

    return border_img


def analyseFace(image, name):
    fixed_image = fixFacePosition(image)

    # print("fim")
    return True


if __name__ == "__main__":
    print("Começando analise")

    expressions = os.listdir(DATASET_PATH)
    for exp in expressions:
        types = os.listdir(DATASET_PATH + "/"+exp)
        for tp in types:
            users = os.listdir(DATASET_PATH + "/"+exp+"/"+tp)
            for user in users:
                photos = os.listdir(DATASET_PATH + "/"+exp+"/"+tp+"/"+user)
                print(user)
                print(photos)
                print()
                for pht in photos:
                    path = DATASET_PATH + "/"+exp+"/"+tp+"/"+user+"/"+pht

                    img = cv2.imread(path)
                    analyseFace(img, pht)
