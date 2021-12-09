import pandas as pd
import numpy as np
from tqdm import tqdm
import math


from distances_module import self_distance
from prc_folders import users_list
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

def compare_masks(mask_ref,mask_comp):
    dists_obj = self_distance("00","00","04435")
    for i in range (len(mask_ref["x"])):
        x_o = int(mask_ref["x"][i])
        y_o = int(mask_ref["y"][i])
        for j in range (len(mask_comp["x"])):
            x_d = int(mask_comp["x"][j])
            y_d = int(mask_comp["y"][j])
            dist = get_distance(x_o,y_o,x_d,y_d)
            dists_obj.add_distance(i,j,dist)
    return dists_obj

def save_results(df,user,exp_ref,exp_comp,tp_ref,tp_comp):
    try:
        os.mkdir(PATTERN_TEST_PATH+"/"+user)
    except:
        None
    df.to_csv(PATTERN_TEST_PATH+"/"+user+"/"+exp_ref+"-"+tp_ref+"_"+exp_comp+"-"+tp_comp+".csv")
if __name__ == "__main__":
    
    for user in tqdm(users_list):
        for i in range(len(emotions_list)):
            exp_ref = "0"+str(i)
            for j in range(2):
                tp_ref = "0" + str(j)
                mean_user_ref = get_mean_mask_data(user= user,expression =exp_ref,supervisioned = tp_ref)
                for k in range(len(emotions_list)):
                    exp_comp = "0"+str(k)
                    for u in range(2):
                        tp_comp = "0" + str(u)
                        if(exp_ref == exp_comp and tp_ref == tp_comp):
                            continue
                        mean_user_comp = get_mean_mask_data(user= user,expression =exp_comp,supervisioned = tp_comp)
                        dists_obj = compare_masks(mean_user_ref,mean_user_comp)
                        dists_df = dists_obj.get_dataframe()
                        save_results(dists_df,user,exp_ref,exp_comp,tp_ref,tp_comp)
    '''neutral_mean_mask = get_mean_mask_data(user= "04435",expression ="00",supervisioned = "00")
    dists_obj = compare_masks(neutral_mean_mask,neutral_mean_mask)
    dists_df = dists_obj.get_dataframe()
    print(dists_df)
    dists_df.to_csv("data.csv")'''
