from face_adjustments import FaceAdjuster
from face_mash import FaceMashDetector
from definitions import *
from triangles import TRIANGLES

import os
import cv2
import numpy as np
import math
from tqdm import tqdm

import pandas as pd

from multiprocessing import Process

DATASET_PATH = r"D:\OneDrive - UFSC\Academico\UFSC\MIGMA\migma_dataset"


def analyseFace(image, extractor):
    # print("analyseFace")
    row, col = image.shape[:2]
    img_new_width = initial_image_width
    rt = img_new_width/col
    image = cv2.resize(image, (img_new_width, int(row*rt)))
    #cv2.imshow("image", image)
    # cv2.waitKey(0)
    lms = extractor.findFaceMesh(image.copy())
    if(not lms):
        print("\nNo faces")
        return [], "No Faces detected"
    lms = lms[0]
    # --------------------------------------------------------------------------
    adjuster = FaceAdjuster(image.copy(), lms)
    _, succeed = adjuster.alignEyes()
    if not succeed:
        return [], adjuster.error
    _, succeed = adjuster.alignFace()
    if not succeed:
        return [], adjuster.error
    _, succeed = adjuster.faceCrop()
    if not succeed:
        return [], adjuster.error
    _, succeed = adjuster.alignFace()
    if not succeed:
        return [], adjuster.error
    _, succeed = adjuster.fixImageSizeWitBorders()
    if not succeed:
        return [], adjuster.error

    nlms = adjuster.getLms()

    return nlms, None


def handleUser(exp, tp, user, landmarks_extractor):
    try:
        os.mkdir("../processed/"+exp+"/"+tp+"/"+user)
    except:
        user
        return
    try:
        photos = os.listdir(DATASET_PATH + "/"+exp+"/"+tp+"/"+user)
    except:
        print("\nPasta inacessível: " +
              DATASET_PATH + "/"+exp+"/"+tp+"/"+user)
        return
    for pht in photos:
        df = pd.DataFrame()

        try:
            path = DATASET_PATH + "/"+exp+"/"+tp+"/"+user+"/"+pht
        except:
            print("\nPasta inacessível: " +
                  DATASET_PATH + "/"+exp+"/"+tp+"/"+user)
            break

        try:
            lms, err = analyseFace(
                cv2.imread(path), landmarks_extractor)
        except Exception as exception:
            err = type(exception).__name__
            print()
            print(err)

        # lida com o erro da analise
        if(err is not None):
            df["Error"] = np.array([str(err)])
            print("Erro na img " + pht + " do user " +
                  user + " no tipo " + tp + " da exp " + exp)
            df.to_csv("../processed/"+exp+"/"+tp +
                      "/"+user+"/error-"+pht.split(".")[0]+".csv")
            continue
        # print(lms)

        # salva o resultado num df e coloca num csv
        x_list = []
        y_list = []
        for lm in lms:
            x_list.append(lm[0])
            y_list.append(lm[1])
        df["x"] = np.array(x_list)
        df["y"] = np.array(y_list)
        # print(lm)
        df.to_csv("../processed/"+exp+"/"+tp +
                  "/"+user+"/data-lms-"+pht.split(".")[0]+".csv")


def analysisProcessHandler():
    expressions = os.listdir(DATASET_PATH)
    landmarks_extractor = FaceMashDetector()
    for exp in expressions:
        try:
            os.mkdir("../processed/"+exp)
        except:
            exp
        types = os.listdir(DATASET_PATH + "/"+exp)
        for tp in types:
            try:
                os.mkdir("../processed/"+exp+"/"+tp)
            except:
                tp
            print("Tipo: ", tp)
            users = os.listdir(DATASET_PATH + "/"+exp+"/"+tp)
            for user in tqdm(users):
                handleUser(exp, tp, user, landmarks_extractor)


if __name__ == "__main__":
    print("Começando analise")
    processes = []
    for i in range(5):
        print("Registrando processo paralelo:" + str(i))
        processes.append(Process(target=analysisProcessHandler))

    for process in processes:
        process.start()

    for process in processes:
        process.join()


'''landmarks_extractor = FaceMashDetector()
handleUser("00", "00", "01235", landmarks_extractor)'''
