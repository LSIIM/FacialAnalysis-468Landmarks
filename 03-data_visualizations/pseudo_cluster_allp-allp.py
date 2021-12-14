import pandas as pd
import numpy as np
from tqdm import tqdm
import math
from multiprocessing import Process
import os
import plotly.express as px


from inspect import getsourcefile
import os.path
import sys
current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir)
from definitions import *


if __name__ == "__main__":
    form_by_user = pd.read_csv(FORMS_PATH+"/total_scores_by_user.csv", index_col=[0])
    users = os.listdir(PATTERN_TEST_PATH)
    
    df_plot = pd.DataFrame()
    z = ""
    for col in form_by_user:
        if(col == "id_user"):
            continue
        # Os resultados do diff são iguais p todas as expressões
        #for i in range(8):
        #    for j in range(2):
        i = 0
        j = 0
        x = []
        y = []
        for user in tqdm(users):  
            user_results = form_by_user.query(f'id_user == {int(user)}')
            mean_diff_dist = pd.read_csv(PATTERN_TEST_PATH+"/"+user+"/means/mean-diff-dists_allp-allp.csv")
            
            diff_dist = mean_diff_dist.query(f'exp == {i} & tp == {j}')["face"]
            
            try:
                res = user_results[col].tolist()[0]
            except:
                print(user, ": Não fez a coleta")
                continue

            try:
                diff_face = diff_dist.tolist()[0]
            except:
                print(user, ": não possui dados")
                continue
            
            x.append(res)
            y.append(diff_face)

        name = "diff " +str(i)+"-"+str(j)
        z = name
        df_plot[col] = np.array(x)
        df_plot[name] = np.array(y)
        #fig = px.scatter(df_plot, x=col, y=name)
        #fig.write_image("./results/"+col+"_"+name+".png")
    print(form_by_user.columns)
    for i in range(1,len(form_by_user.columns)-1):
        for j in range(i+1,len(form_by_user.columns)):
            col1 = form_by_user.columns[i]
            col2 = form_by_user.columns[j]
            fig = px.scatter_3d(df_plot, x=col1, y=col2, z=z)
            fig.update_traces(marker={'size': 4})
            fig.write_html("./results/3d-"+col1+"-"+col2+"_"+name+".html")
            fig.write_image("./results/3d-"+col1+"-"+col2+"_"+name+".png",width=1000, height=1300)