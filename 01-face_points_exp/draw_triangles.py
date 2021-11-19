
from triangles import TRIANGLES
import os
import numpy as np
import pandas as pd
import cv2

expressions = os.listdir("../processed")
for exp in expressions:
    mean_exp = np.zeros((600, 600, 3), dtype=float)
    num = 0
    if(len(exp.split(".")) > 1):
        continue
    types = os.listdir("../processed/"+exp)
    for tp in types:
        if(len(tp.split(".")) > 1):
            continue
        users = os.listdir("../processed/"+exp+"/"+tp)
        for user in users:
            infos = os.listdir("../processed/"+exp+"/"+tp+"/"+user)
            mean_user = np.zeros((600, 600, 3), dtype=float)
            for doc in infos:
                if(doc.split(".")[1] == "csv"):
                    df = pd.read_csv("../processed/"+exp +
                                     "/"+tp+"/"+user+"/"+doc)
                    image = np.zeros((600, 600, 3), dtype=float)
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
                    cv2.imwrite("../processed/"+exp +
                                "/"+tp+"/"+user+"/" + doc.split(".")[0]+'.jpg', image)
                    cv2.imshow("img", image)
                    mean_user = mean_user + image
                    mean_exp = mean_exp + image
                    num += 1
                    cv2.waitKey(1)
            mean_user /= 3
            mean_user *= -1
            mean_user += 255
            mean_user = np.array(mean_user, dtype=np.uint8)
            cv2.imwrite("../processed/"+exp +
                        "/"+tp+"/"+user+"/" + "mean_" + user + ".jpg", mean_user)
            cv2.imshow("Mean User", mean_user)
            # cv2.waitKey(0)
    mean_exp /= num
    mean_exp *= -1
    mean_exp += 255
    mean_exp = np.array(mean_exp, dtype=np.uint8)
    cv2.imwrite("../processed/"+exp + "/mean_" + exp + ".jpg", mean_exp)
    cv2.imshow("Mean Exp", mean_exp)
    # cv2.waitKey(0)
