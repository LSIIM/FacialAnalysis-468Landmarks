import pandas as pd
import numpy as np
from tqdm import tqdm
import math
from multiprocessing import Process


from distances_module import MaskDistances
from inspect import getsourcefile
import os.path
import sys
current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir)
from definitions import *

class MeanDistances():
    def __init__(self, emotion, tp):
        self.emotion = "0"+str(emotion)
        self.tp = "0"+str(tp)
        self.df = pd.DataFrame()
        self.qtd_masks = 0

    def verify_mask_type(self, arq_name):
        exp,tp = arq_name.split("_")[0].split("-")
        return exp == self.emotion and tp == self.tp
    def add_distances(self,dist_df):
        new_dists = np.array(dist_df["distances"])
        if(len(self.df)==0):
            old_dists = np.zeros(new_dists.shape)
        else:
            old_dists = np.array(self.df["distances"])
        self.df["distances"] = old_dists + new_dists
        self.qtd_masks+=1
        return    

    def calculate_means(self):
        
        old_dists = np.array(self.df["distances"])
        self.df["distances"] = old_dists/self.qtd_masks

        return

    def get_dataframe(self):
        return self.df
    
    def save_dataframe(self):
        try:
            os.mkdir("./results/"+self.emotion+"-"+self.tp)
        except:
            None
        self.df.to_csv("./results/"+self.emotion+"-"+self.tp+"/distances-stats.csv")

if __name__ == "__main__":
    
    users = os.listdir(PATTERN_TEST_PATH)
    saves = []
    for i in range(8):
        for j in range(2):
            saves.append(MeanDistances(i,j))
    
    for user in tqdm(users):
        arqs = os.listdir(PATTERN_TEST_PATH+"/"+user)
        for arq in arqs:
            if(arq.split(".")[1] != "csv"):
                continue

            df = pd.read_csv(PATTERN_TEST_PATH+"/"+user+"/"+arq)
            for i in range(len(saves)):
                if(saves[i].verify_mask_type(arq)):
                    saves[i].add_distances(df)
                    break
    for i in range(len(saves)):
        saves[i].calculate_means()
        saves[i].save_dataframe()