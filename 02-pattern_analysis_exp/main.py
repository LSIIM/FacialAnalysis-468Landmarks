import pandas as pd
import numpy as np
from tqdm import tqdm
import math


from distances_module import self_distance

from inspect import getsourcefile
import os.path
import sys
current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir)
from definitions import *


def get_mask_data(user= "04435",expression ="00",supervisioned = "00"):
    arqs = os.listdir(PROCESSED_PATH+"/"+expression+"/"+supervisioned+"/"+user)
    csvs = []
    for arq in arqs:
        if(len(arq.split("data-lms"))>1 and arq.split(".")[1] == "csv"):
            csvs.append(arq)
    dfs = []
    for x in csvs:
        dfs.append(df)
    return dfs

def get_mean_mask_data(user= "04435",expression ="00",supervisioned = "00"):
    arqs = os.listdir(PROCESSED_PATH+"/"+expression+"/"+supervisioned+"/"+user)
    for arq in arqs:
        if(len(arq.split("mean-lms"))>1 and arq.split(".")[1] == "csv"):
            df = pd.read_csv(PROCESSED_PATH+"/"+expression+"/"+supervisioned+"/"+user+"/"+arq)
            return df
    

def get_distance(x_o,y_o,x_d,y_d):
    return math.sqrt( (x_d-x_o)**2 + (y_d-y_o)**2) 

if __name__ == "__main__":
    #neutral_masks = get_masks_data(user= "04435",expression ="00",supervisioned = "00")
    #for j in range(len(emotions_list)):
    #exp = str(j)+str(j)
    neutral_mean_mask = get_mean_mask_data(user= "04435",expression ="00",supervisioned = "00")
    dists_obj = self_distance("00","00","04435")
    for i in range (len(neutral_mean_mask["x"])):
        x_o = int(neutral_mean_mask["x"][i])
        y_o = int(neutral_mean_mask["y"][i])
        for j in range (len(neutral_mean_mask["x"])):
            x_d = int(neutral_mean_mask["x"][j])
            y_d = int(neutral_mean_mask["y"][j])
            dist = get_distance(x_o,y_o,x_d,y_d)
            dists_obj.add_distance(i,j,dist)
    dists_df = dists_obj.get_dataframe()
    print(dists_df)
    dists_df.to_csv("data.csv")
