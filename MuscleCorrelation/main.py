from FaceMeshModule import FaceMeshDetector
import cv2
import pandas as pd
import numpy as np
from muscles_identification import *


def detect_face_on_image(path):
    detector = FaceMeshDetector(maxNumFaces=1, minDetectionConfidence=0.8)
    name = path.split('/')
    name = name[len(name)-1].split('.')
    name = name[0]
    img = cv2.imread(path)
    img_f, faces = detector.findFaceMesh(img)
    print(name)
    #cv2.namedWindow('Muscles', cv2.WINDOW_NORMAL)

    while(1):
        img2 = img_f.copy()
        muscles = get_muscles_from_csv()
        for face in faces:
            for i, lms in enumerate(face):
                achou = False
                for muscle in muscles:
                    if(i in muscle.muscle_points):
                        achou = True
                        cv2.putText(img2, ".", lms,
                                    cv2.FONT_HERSHEY_PLAIN, 8, (0, 0, 0), 4)
                        cv2.putText(img2, str(i), lms,
                                    cv2.FONT_HERSHEY_PLAIN, 2, muscle.color, 1)
                        break
                if(not achou):
                    cv2.putText(img2, str(i), lms,
                                cv2.FONT_HERSHEY_PLAIN, 1.6, (0, 255, 0), 1)

        cv2.putText(img2, "Legenda de cores", (100, 300),
                    cv2.FONT_HERSHEY_PLAIN, 10, (0, 0, 0), 3)
        for i, muscle in enumerate(muscles):
            cv2.putText(img2, muscle.muscle_name, (100, 500 + 200*i),
                        cv2.FONT_HERSHEY_PLAIN, 10, muscle.color, 3)
        cv2.imshow("Muscles", cv2.resize(
            img2, (1000, 1000), interpolation=cv2.INTER_AREA))
        cv2.waitKey(1)
        cv2.imwrite(name+"-landmarks-colored.jpg", img2)


if __name__ == "__main__":
    detect_face_on_image("./human-muscles.jpg")
