from cmath import exp
import pandas as pd
import numpy as np
from tqdm import tqdm
import os

from definitions import *




if __name__ == "__main__":
    users = os.listdir(PATTERN_TEST_PATH)
    for user in tqdm(users):
        #print(user)
        try:
            os.mkdir(PATTERN_TEST_PATH_SAME_POINT+"/"+user)
        except:
            None
        masks_dists = os.listdir(PATTERN_TEST_PATH+"/"+user)
        for mask_dist in masks_dists:
            if(len(mask_dist.split("."))==2):
                #print(mask_dist)
                old_df = pd.read_csv(PATTERN_TEST_PATH+"/"+user+"/"+mask_dist, index_col=0)
                new_df = old_df[old_df.origins == old_df.destinations]
                new_df.to_csv(PATTERN_TEST_PATH_SAME_POINT+"/"+user+"/"+mask_dist)
    