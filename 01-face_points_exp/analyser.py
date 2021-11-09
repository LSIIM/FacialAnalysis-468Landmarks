from face_adjustments import FaceAdjuster
from face_mash import FaceMashDetector
import os
import cv2

DATASET_PATH = r"D:\OneDrive - Etec Centro Paula Souza\Academico\UFSC\MIGMA\migma_dataset"


def analyseFace(image, name):
    meshed = FaceMashDetector(image=image)
    if(not meshed.findFaceMesh()):
        return False

    lms = meshed.getLms()

    adjuster = FaceAdjuster(image, lms[0])
    eyes_cent_img = adjuster.alignEyes()
    cv2.imshow("Olhos", eyes_cent_img)
    cv2.waitKey(0)
    return True


if __name__ == "__main__":
    print("Começando analise")
    test_path = r"D:\OneDrive - Etec Centro Paula Souza\Academico\UFSC\MIGMA\migma_dataset\00\00\01235"
    fotos = os.listdir(test_path)
    path = test_path + "/"+fotos[0]

    img = cv2.imread(path)
    analyseFace(img, fotos[0])
    '''
    expressions = os.listdir(DATASET_PATH)
    for exp in expressions:
        types = os.listdir(DATASET_PATH + "/"+exp)
        for tp in types:
            users = os.listdir(DATASET_PATH + "/"+exp+"/"+tp)
            print(users)
    '''
