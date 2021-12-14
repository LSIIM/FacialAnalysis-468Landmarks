import pandas as pd
import numpy as np
from tqdm import tqdm
import math
from multiprocessing import Process
import os

from distances_module import MaskDistances
from inspect import getsourcefile
import os.path
import sys
current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir)
from definitions import *


def analyse_distances_and_diffs(user):
    exps = []
    tps = []
    diff_dists = []
    mean_dists = []
    dists_files = os.listdir(PATTERN_TEST_PATH+"/"+user)
    for file in dists_files:
        if(file == "means"):
            continue
        df = pd.read_csv(PATTERN_TEST_PATH+"/"+user+"/"+file)
        exp_tp = file.split("_")[0]
        df_mean = pd.read_csv("./results/analysis/"+exp_tp+"/distances-stats.csv", index_col=[0])
        dists = np.array(df_mean["distances"])
        diffs = np.sqrt((dists -np.array(df["distances"]) )**2).mean()
        exp,tp = exp_tp.split("-")
        exps.append(exp)
        tps.append(tp)
        diff_dists.append(diffs)
        mean_dists.append(dists.mean())
    return np.array(exps),np.array(tps),np.array(diffs),np.array(mean_dists)
if __name__ == "__main__":
    users = os.listdir(PATTERN_TEST_PATH)
    
    for user in tqdm(users):
        try:
            os.mkdir(PATTERN_TEST_PATH+"/"+user+"/means/")
        except:
            None
        try:
            mean_diff_dists = pd.read_csv(PATTERN_TEST_PATH+"/"+user+"/means/mean-diff-dists_allp-allp.csv",index_col=[0])
        except:
            mean_diff_dists = pd.DataFrame()
        try:
            mean_dists = pd.read_csv(PATTERN_TEST_PATH+"/"+user+"/means/mean-dists_allp-allp.csv",index_col=[0])
        except:
            mean_dists = pd.DataFrame()
        
        exps,tps,diffs,dists = analyse_distances_and_diffs(user)


        mean_diff_dists["exp"] = exps
        mean_diff_dists["tp"] = tps

        mean_diff_dists["face"] = diffs
        mean_diff_dists.to_csv(PATTERN_TEST_PATH+"/"+user+"/means/mean-diff-dists_allp-allp.csv")

        mean_dists["exp"] = exps
        mean_dists["tp"] = tps

        mean_dists["face"] = dists
        mean_dists.to_csv(PATTERN_TEST_PATH+"/"+user+"/means/mean-dists_allp-allp.csv")
        
