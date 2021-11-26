import cv2
import numpy as np
from tqdm import tqdm
import os
from definitions import *

vfps = 30.0
frames_image = 15
fourcc = cv2.VideoWriter_fourcc(*'MPEG')
video_h = int(final_image_size_height/3)
video_w = int((final_image_size_width*2)/3)
out = cv2.VideoWriter(DATASET_PATH+"/faces-video.avi", fourcc,
                      vfps, (int(video_w), int(video_h)))
print((int(video_w), int(video_h)))
if out is None:
    print("Erro na criação do escritor")
else:
    expressions = os.listdir(PROCESSED_PATH)
    for exp in expressions:
        if(len(exp.split(".")) > 1):
            continue
        types = os.listdir(PROCESSED_PATH + "/"+exp)
        for tp in types:
            if(len(tp.split(".")) > 1):
                continue
            users = os.listdir(PROCESSED_PATH + "/"+exp+"/"+tp)
            frame = np.zeros((int(video_h),
                              int(video_w), 3), dtype="uint8")
            cv2.putText(frame, exp+"/"+tp, (
                        int(((video_w/2) * 3)/4), int(video_h/2)), cv2.FONT_HERSHEY_PLAIN, 10, (255, 255, 255), 3)
            print(frame.shape)
            for i in range(int(vfps) * 2):
                out.write(frame)
                # frame1 = cv2.resize(frame,
                #                   (int(video_w/3), int(video_h/3)))
                # cv2.imshow("fr", frame1)
                # cv2.waitKey(0)
            for user in tqdm(users):
                if(len(user.split(".")) > 1):
                    continue
                photos = os.listdir(PROCESSED_PATH + "/"+exp+"/"+tp+"/"+user)
                faces = []
                masks = []
                for pht in photos:
                    if(pht.split(".")[1] == "csv" or pht.split("-")[0] == "mean"):
                        continue
                    path = PROCESSED_PATH + "/"+exp+"/"+tp+"/"+user + "/"+pht
                    img = cv2.imread(path)
                    if(pht.split("-")[0] == "data"):
                        masks.append(img)
                    if(pht.split("-")[0] == "face"):
                        faces.append(img)
                if(len(faces) != len(masks)):
                    print("ERRO DE QUANTIDADE DE IMAGENS!!!!!!")
                    break
                for i in range(len(faces)):
                    img = faces[i]
                    cdif = final_image_size_width - img.shape[1]
                    rdif = final_image_size_height - img.shape[0]
                    border = cv2.copyMakeBorder(
                        img,
                        top=int(rdif/2),
                        bottom=int(rdif/2),
                        left=int(cdif/2),
                        right=int(cdif/2),
                        borderType=cv2.BORDER_CONSTANT,
                        value=[0, 0, 0]
                    )
                    border = cv2.resize(
                        border, (int((video_w/2)), int(video_h)))
                    mask_img = cv2.resize(
                        masks[i], (int((video_w/2)), int(video_h)))
                    frame = np.hstack(
                        (border, mask_img))
                    frame = cv2.resize(
                        frame, (int(video_w), int(video_h)))
                    frame = np.array(frame, dtype="uint8")

                    cv2.putText(frame, exp+"/"+tp, (
                        int(video_w*5/11), int(video_h*3/5)), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 1)

                    cv2.putText(frame, user, (
                        int(video_w*5/11), int(video_h*4/5)), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 1)
                    for j in range(frames_image):
                        out.write(frame)
                    # frame = cv2.resize(frame,
                    #                   (int(video_w/3), int(video_h/3)))
                    # cv2.imshow("fr", frame)
                    # cv2.waitKey(1)

out.release()
