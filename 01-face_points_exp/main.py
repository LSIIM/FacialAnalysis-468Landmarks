import cv2
import numpy as np
from numpy.core.fromnumeric import shape
from scipy import ndimage
import math
import cv2
from tqdm import tqdm

print(cv2.__version__)
for i in tqdm(range(1000000000)):
    img = cv2.imread(
        r"D:\OneDrive - Etec Centro Paula Souza\Academico\UFSC\MIGMA\migma_dataset\00\00\00001\2019-03-14 13_59_51.jpg")
