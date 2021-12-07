import pandas as pd
import numpy as np

class self_distance():
    def __init__(self, exp_reference, exp_comp, user):
        self.exp_reference = exp_reference
        self.exp_comp = exp_comp
        self.user = user
        self.distances = [] # [[origin, destination, distance(pixels)]]
    
    def add_distance(self,origin, destination, dist):
        self.distances.append([int(origin),int(destination),int(dist)])
    
    def get_dataframe(self):
        origins = []
        destinations = []
        distances = []
        for dt in self.distances:
            orig,dest,dist = dt
            origins.append(orig)
            destinations.append(dest)
            distances.append(dist)
        df = pd.DataFrame()
        
        df["origins"] = np.array(origins)
        df["destinations"] = np.array(destinations)
        df["distances"] = np.array(distances)
        return df