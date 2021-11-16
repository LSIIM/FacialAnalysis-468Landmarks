
import os

import shutil
expressions = os.listdir("../processed")
for exp in expressions:
    types = os.listdir("../processed/"+exp)
    for tp in types:
        users = os.listdir("../processed/"+exp+"/"+tp)
        for user in users:
            infos = os.listdir("../processed/"+exp+"/"+tp+"/"+user)
            if(len(infos) == 0):
                print("Removendo pasta vazia: "+exp+"/"+tp+"/"+user)
                shutil.rmtree("../processed/"+exp+"/"+tp+"/"+user)
                continue

            if(len(infos) != 3):
                print("Removendo pasta com numero incorreto de imagens: " +
                      exp+"/"+tp+"/"+user)
                shutil.rmtree("../processed/"+exp+"/"+tp+"/"+user)
            achou = False
            for nm in infos:
                if(nm.split("-")[0] == "error"):
                    achou = True
                    break
            if(achou):
                print("Removendo pasta com erros: "+exp+"/"+tp+"/"+user)
                shutil.rmtree("../processed/"+exp+"/"+tp+"/"+user)
