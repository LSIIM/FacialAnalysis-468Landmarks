import pandas as pd
import numpy as np
import os
class MaskStats():
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
            self.df["origins"] = dist_df["origins"]
            self.df["destinations"] = dist_df["destinations"]
        else:
            old_dists = np.array(self.df["distances"])
        self.df["distances"] = old_dists + new_dists
        self.qtd_masks+=1
        return    

    def calculate_dist_means(self):
        old_dists = np.array(self.df["distances"])
        self.df["distances"] = old_dists/self.qtd_masks
        return

    def calculate_deviation_means(self):
        old_deviations = np.array(self.df["std_deviation"])
        self.df["std_deviation"] = old_deviations/self.qtd_masks
        return
    
    def add_std_deviation(self,dist_df):
        
        new_dists = np.array(dist_df["distances"])
        mean_dists = np.array(self.df["distances"])
        dists_dif = mean_dists - new_dists
        deviation = np.sqrt((dists_dif)**2)
        
        self.df["std_deviation"] = np.array(self.df["std_deviation"]) + deviation
        self.qtd_masks+=1
    def get_dataframe(self):
        return self.df
    def load_df(self):
        df = pd.read_csv("./results/analysis/"+self.emotion+"-"+self.tp+"/distances-stats.csv")
        self.df["origins"] = df["origins"]
        self.df["destinations"] = df["destinations"]
        self.df["distances"] = df["distances"]
        self.df["std_deviation"] = np.zeros(np.array(df["distances"]).shape)

    
    def save_dataframe(self):
        try:
            os.mkdir("./results/analysis/"+self.emotion+"-"+self.tp)
        except:
            None
        self.df.to_csv("./results/analysis/"+self.emotion+"-"+self.tp+"/distances-stats.csv")