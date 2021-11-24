
from triangles import TRIANGLES
import os
import numpy as np
import pandas as pd
import cv2
from definitions import *
from tqdm import tqdm


def convert_to_ghost(image, num, path):
    image = np.array(image, dtype=float)
    image /= num
    image *= -1
    image += 255
    image = np.array(image, dtype=np.uint8)
    cv2.imwrite(path, image)


def drawImage(df, path):
    image = np.zeros(
        (final_image_size_height, final_image_size_width, 3), dtype=float)
    x = df["x"].tolist()
    y = df["y"].tolist()
    lms = []
    for i in range(len(x)):
        lms.append([x[i], y[i]])
    for tria in TRIANGLES:
        image = cv2.line(image, lms[tria[0]],
                         lms[tria[1]], (255, 255, 255), 1)
        image = cv2.line(image, lms[tria[0]],
                         lms[tria[2]], (255, 255, 255), 1)
        image = cv2.line(image, lms[tria[1]],
                         lms[tria[2]], (255, 255, 255), 1)
    cv2.imwrite(path, image)
    return image


expressions = os.listdir(PROCESSED_PATH)
for exp in expressions:
    mean_exp = np.zeros(
        (final_image_size_height, final_image_size_width, 3), dtype=float)
    num = 0
    if(len(exp.split(".")) > 1):
        continue
    types = os.listdir(PROCESSED_PATH + "/"+exp)
    for tp in types:
        if(len(tp.split(".")) > 1):
            if(tp.split(".")[1] == "csv"):
                df = pd.read_csv(PROCESSED_PATH + "/"+exp+"/"+tp)
                image = drawImage(df, PROCESSED_PATH + "/"+exp +
                                  "/" + tp.split(".")[0]+'.jpg')
            continue
        users = os.listdir(PROCESSED_PATH + "/"+exp+"/"+tp)
        mean_exp_tp = np.zeros(
            (final_image_size_height, final_image_size_width, 3), dtype=float)
        num_users_images = 0
        for user in tqdm(users):
            if(len(user.split(".")) > 1):
                if(user.split(".")[1] == "csv"):
                    df = pd.read_csv(PROCESSED_PATH + "/"+exp+"/"+tp+"/"+user)
                    image = drawImage(df, PROCESSED_PATH + "/"+exp +
                                      "/"+tp+"/" + tp.split(".")[0]+'.jpg')
                continue
            infos = os.listdir(PROCESSED_PATH + "/"+exp+"/"+tp+"/"+user)
            mean_user = np.zeros(
                (final_image_size_height, final_image_size_width, 3), dtype=float)
            for doc in infos:
                if(doc.split(".")[1] == "csv"):
                    df = pd.read_csv(PROCESSED_PATH + "/"+exp +
                                     "/"+tp+"/"+user+"/"+doc)
                    image = drawImage(df, PROCESSED_PATH + "/"+exp +
                                      "/"+tp+"/"+user+"/" + doc.split(".")[0]+'.jpg')
                    #cv2.imshow("img", image)
                    mean_user += image
                    mean_exp += image
                    mean_exp_tp += image
                    num += 1
                    num_users_images += 1
                    # cv2.waitKey(1)
            mean_user = np.array(mean_user, dtype=np.uint8)
            convert_to_ghost(mean_user, 3, PROCESSED_PATH + "/"+exp +
                             "/"+tp+"/"+user+"/" + "mean_" + user + ".jpg")

        convert_to_ghost(mean_exp_tp, num_users_images, PROCESSED_PATH + "/"+exp+"/"+tp + "/mean_" +
                         exp + "-"+tp + ".jpg")

    convert_to_ghost(mean_exp, num, PROCESSED_PATH +
                     "/"+exp + "/mean_" + exp + ".jpg")
