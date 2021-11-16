from face_adjustments import FaceAdjuster
from face_mash import FaceMashDetector


import os
import cv2
import numpy as np
import math
from tqdm import tqdm

import pandas as pd

from multiprocessing import Process

DATASET_PATH = r"D:\OneDrive - Etec Centro Paula Souza\Academico\UFSC\MIGMA\migma_dataset"


def analyseFace(image, extractor):
    gc.collect()
    row, col = image.shape[:2]
    img_new_width = 1000
    rt = img_new_width/col
    image = cv2.resize(image, (img_new_width, int(row*rt)))

    lms = extractor.findFaceMesh(image.copy())
    if(not lms):
        print("No faces")
        cv2.imshow("Erro", image)
        cv2.waitKey(0)
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
                try:
                    os.mkdir("../processed/"+exp+"/"+tp+"/"+user)
                except:
                    user
                    continue
                photos = os.listdir(DATASET_PATH + "/"+exp+"/"+tp+"/"+user)
                for pht in photos:
                    df = pd.DataFrame()
                    path = DATASET_PATH + "/"+exp+"/"+tp+"/"+user+"/"+pht
                    try:
                        lms, err = analyseFace(
                            cv2.imread(path), landmarks_extractor)
                    except:
                        print("Erro de memoria")
                        continue

                    # lida com o erro da analise
                    if(err is not None):
                        df["Error"] = err
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


if __name__ == "__main__":
    print("Começando analise")
    processes = []
    for i in range(2):
        print("Registrando processo paralelo:" + str(i))
        processes.append(Process(target=analysisProcessHandler))

    for process in processes:
        process.start()

    for process in processes:
        process.join()
