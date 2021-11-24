from face_adjustments import FaceAdjuster
from face_mesh import FaceMeshDetector
from definitions import *

import os
import cv2
import numpy as np
import math
from tqdm import tqdm

import pandas as pd

from multiprocessing import Process


def analyseFace(image, extractor):
    # print("analyseFace")
    row, col = image.shape[:2]
    img_new_width = initial_image_width
    rt = img_new_width/col
    image = cv2.resize(image, (img_new_width, int(row*rt)))

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
        os.mkdir(PROCESSED_PATH + "/"+exp+"/"+tp+"/"+user)
    except:
        user
        return None
    try:
        photos = os.listdir(DATASET_PATH + "/"+exp+"/"+tp+"/"+user)
    except:
        print("\nPasta inacessível: " +
              DATASET_PATH + "/"+exp+"/"+tp+"/"+user)
        return None
    mlms = np.array([np.zeros((468,), dtype=np.uint32),
                    np.zeros((468,), dtype=np.uint32)])
    num = 0
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
            df.to_csv(PROCESSED_PATH + "/"+exp+"/"+tp +
                      "/"+user+"/error-"+pht.split(".")[0]+".csv")
            continue
        # print(lms)

        # salva o resultado num df e coloca num csv
        x_list = []
        y_list = []
        for lm in lms:
            x_list.append(lm[0])
            y_list.append(lm[1])
        xnp = np.array(x_list)
        ynp = np.array(y_list)
        df["x"] = xnp
        df["y"] = ynp
        mlms = np.array([xnp + mlms[0], ynp+mlms[1]], dtype=np.uint32)

        num += 1
        # print(lm)
        df.to_csv(PROCESSED_PATH + "/"+exp+"/"+tp +
                  "/"+user+"/data-lms-"+pht.split(".")[0]+".csv")
    mlms = np.array([mlms[0]//num, mlms[1]//num], dtype=np.uint32)

    return mlms


def analysisProcessHandler():
    expressions = os.listdir(DATASET_PATH)
    landmarks_extractor = FaceMeshDetector()
    for exp in expressions:
        try:
            os.mkdir(PROCESSED_PATH + "/"+exp)
        except:
            exp
        types = os.listdir(DATASET_PATH + "/"+exp)

        mexp_lms = np.array(
            [np.zeros((468,)), np.zeros((468,), dtype=np.uint32)])
        num_tp = 0
        df_mean_exp = pd.DataFrame()
        for tp in types:
            try:
                os.mkdir(PROCESSED_PATH + "/"+exp+"/"+tp)
            except:
                tp
            print("Tipo: ", tp)
            users = os.listdir(DATASET_PATH + "/"+exp+"/"+tp)
            mtp_lms = np.array(
                [np.zeros((468,), dtype=np.uint32), np.zeros((468,), dtype=np.uint32)], dtype=np.uint32)
            df_mean_tp = pd.DataFrame()
            num_users = 0
            for user in tqdm(users):
                mu_lms = handleUser(exp, tp, user, landmarks_extractor)
                if(mu_lms is not None):
                    df_mean_user = pd.DataFrame()
                    df_mean_user["x"] = mu_lms[0]
                    df_mean_user["y"] = mu_lms[1]
                    df_mean_user.to_csv(PROCESSED_PATH + "/"+exp+"/"+tp +
                                        "/"+user+"/mean-lms-"+(user)+".csv")
                    mtp_lms = np.array(
                        [mu_lms[0]+mtp_lms[0], mu_lms[1]+mtp_lms[1]])
                    num_users += 1
            save_mtp_lms = [mtp_lms[0]//num_users, mtp_lms[1]//num_users]
            save_mtp_lms = np.array(save_mtp_lms, dtype=np.uint32)
            df_mean_tp["x"] = save_mtp_lms[0]
            df_mean_tp["y"] = save_mtp_lms[1]
            df_mean_tp.to_csv(PROCESSED_PATH + "/"+exp+"/"+tp
                              + "/mean-lms-"+(tp)+".csv")
            mexp_lms = np.array(
                [mexp_lms[0]+mtp_lms[0], mexp_lms[1]+mtp_lms[1]])
            num_tp += 1
        save_mean_exp = [mexp_lms[0]//num_users, mexp_lms[1]//num_users]
        save_mean_exp = np.array(save_mean_exp, dtype=np.uint32)
        df_mean_exp["x"] = save_mean_exp[0]
        df_mean_exp["y"] = save_mean_exp[1]
        df_mean_exp.to_csv(PROCESSED_PATH + "/"+exp +
                           "/mean-lms-"+(exp)+".csv")


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

'''landmarks_extractor = FaceMeshDetector()
handleUser("05", "01", "00012", landmarks_extractor)'''
