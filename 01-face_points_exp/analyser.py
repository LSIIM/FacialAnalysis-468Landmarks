from face_adjustments import FaceAdjuster
from face_mash import FaceMashDetector
import os
import cv2
import numpy as np

DATASET_PATH = r"D:\OneDrive - Etec Centro Paula Souza\Academico\UFSC\MIGMA\migma_dataset"


def fixFacePosition(image):
    meshed_orig = FaceMashDetector(image=image)
    if(not meshed_orig.findFaceMesh()):
        return False

    lms_orig = meshed_orig.getLms()

    adjuster = FaceAdjuster(image, lms_orig[0])
    eyes_cent_img = adjuster.alignEyes()

    meshed_forehead = FaceMashDetector(image=eyes_cent_img)
    if(not meshed_forehead.findFaceMesh()):
        return False

    lms_forehead = meshed_forehead.getLms()
    if(lms_forehead == []):
        print("Erro, nenhum rosto detectado")
        return None
    else:
        lms_forehead = lms_forehead[0]
    adjuster = FaceAdjuster(eyes_cent_img, lms_forehead)
    eyes_forehead_fix = adjuster.alignFace()

    meshed_crop = FaceMashDetector(image=eyes_forehead_fix)
    if(not meshed_crop.findFaceMesh()):
        return False

    lms_crop = meshed_crop.getLms()
    if(lms_crop == []):
        print("Erro, nenhum rosto detectado")
        return None
    else:
        lms_crop = lms_crop[0]
    adjuster = FaceAdjuster(eyes_forehead_fix, lms_crop)
    crop_image = adjuster.faceCrop()

    meshed_final = FaceMashDetector(image=crop_image)
    if(not meshed_final.findFaceMesh()):
        return False

    lms_final = meshed_final.getLms()
    if(lms_final == []):
        print("Erro, nenhum rosto detectado")
        return None
    else:
        lms_final = lms_final[0]
    print(lms_final[10])

    # -------- Teste -----------------
    #cv2.imshow("orig", image)
    cv2.imshow("crop", crop_image)
    cv2.waitKey(0)
    # ---------------------------------
    return eyes_cent_img


def analyseFace(image, name):
    fixed_image = fixFacePosition(image)

    return True


if __name__ == "__main__":
    print("Começando analise")
    test_path = r"D:\OneDrive - Etec Centro Paula Souza\Academico\UFSC\MIGMA\migma_dataset\00\00\04438"
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
