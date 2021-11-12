from face_adjustments import FaceAdjuster
from face_mash import FaceMashDetector
import os
import cv2
import numpy as np
import math
from tqdm import tqdm
import plotly.graph_objects as go
import plotly.express as px
from multiprocessing import Process
import pandas as pd
from memory_profiler import profile
DATASET_PATH = r"D:\OneDrive - Etec Centro Paula Souza\Academico\UFSC\MIGMA\migma_dataset"


def analyseFace(image):
    # print(image.shape)
    #print((int(image.shape[0]/2), int(image.shape[1]/2)))
    row, col = image.shape[:2]
    img_new_width = 600
    rt = img_new_width/col
    image = cv2.resize(image, (img_new_width, int(row*rt)))

    meshed = FaceMashDetector(image=image)
    if(not meshed.findFaceMesh()):
        print("No faces")
        cv2.imshow("Erro", image)
        cv2.waitKey(0)
        return [], "No Faces detected"

    lms = meshed.getLms()[0]

    # --------------------------------------------------------------------------
    adjuster = FaceAdjuster(image, lms)
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

    # print("------------------------------------------------------------")
    # -------- Teste -----------------
    # cv2.imshow("orig", image)
    # print("Crop")
    # print(nlms[10])
    # print(nlms[152][1]-nlms[10][1])
    # for i in range(len(nlms)):
    #    cv2.putText(border_img, ".", nlms[i], cv2.FONT_HERSHEY_PLAIN,
    #                0.8, (0, 255, 0), 1)

    #cv2.imshow("img", border_img)
    # cv2.waitKey(1)
    # ---------------------------------
    del image
    return adjuster.getLms(), None


def analysisProcessHandler():
    expressions = os.listdir(DATASET_PATH)
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
                df = pd.DataFrame()
                lm_lists = []
                for pht in photos:
                    path = DATASET_PATH + "/"+exp+"/"+tp+"/"+user+"/"+pht

                    lms, err = analyseFace(cv2.imread(path))
                    if(err):
                        df["Error"] = err
                        print("Erro na img " + pht + " do user " +
                              user + " no tipo " + tp + " da exp " + exp)
                        df.to_csv("../processed/"+exp+"/"+tp +
                                  "/"+user+"/error-"+pht.split(".")[0]+".csv")
                        continue
                    # print(lms)
                    lm_lists.append(lms)

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
