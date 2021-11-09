from face_adjustments import FaceAdjuster
from face_mash import FaceMashDetector
import os
import cv2

DATASET_PATH = r"D:\OneDrive - Etec Centro Paula Souza\Academico\UFSC\MIGMA\migma_dataset"


def image_resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image

    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)

    else:
        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv2.resize(image, dim, interpolation=inter)
    return resized


def analyseFace(image, name):
    meshed_orig = FaceMashDetector(image=image)
    if(not meshed_orig.findFaceMesh()):
        return False

    lms_orig = meshed_orig.getLms()

    adjuster = FaceAdjuster(image, lms_orig[0])
    eyes_cent_img = adjuster.alignEyes()
    eyes_cent_img = image_resize(eyes_cent_img, height=550)
    #cv2.imshow("orig", image)
    cv2.imshow("Olhos", eyes_cent_img)
    cv2.waitKey(0)
    meshed_crop = FaceMashDetector(image=eyes_cent_img)
    if(not meshed_crop.findFaceMesh()):
        return False

    drawImg = eyes_cent_img.copy()
    lms_crop = meshed_crop.getLms()
    for lm in lms_crop[0]:
        cv2.putText(drawImg, ".", lm, cv2.FONT_HERSHEY_PLAIN,
                    0.8, (0, 255, 0), 1)
    cv2.imshow("new_face", drawImg)
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
