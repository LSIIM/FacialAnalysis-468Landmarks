from face_adjustments import FaceAdjuster
from face_mash import FaceMashDetector
import os

DATASET_PATH = "D:\OneDrive - Etec Centro Paula Souza\Academico\UFSC\MIGMA\migma_dataset"


def analyseFace(image):
    meshed = FaceMashDetector(image=image)
    meshed.findFaceMesh()
    lms = meshed.getLms()
    for face in lms:
        print(face)
    return


if __name__ == "__main__":
    print("Começando analise")
    print(os.listdir(DATASET_PATH))
