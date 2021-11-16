
import os

import shutil

delete = input("Desseja deletar as inconsistencias detectadas? s/n   ")
delete = delete == "s" or delete == "S"
num_incorreto = 0
pasta_vazia = 0
com_erro = 0
expressions = os.listdir("../processed")
for exp in expressions:
    types = os.listdir("../processed/"+exp)
    for tp in types:
        users = os.listdir("../processed/"+exp+"/"+tp)
        for user in users:
            infos = os.listdir("../processed/"+exp+"/"+tp+"/"+user)
            if(len(infos) == 0):
                print("Removendo pasta vazia: "+exp+"/"+tp+"/"+user)
                if(delete):
                    shutil.rmtree("../processed/"+exp+"/"+tp+"/"+user)
                pasta_vazia += 1
                continue

            if(len(infos) != 3):
                print("Removendo pasta com numero incorreto de imagens: " +
                      exp+"/"+tp+"/"+user)
                if(delete):
                    shutil.rmtree("../processed/"+exp+"/"+tp+"/"+user)
                num_incorreto += 1
                continue
            achou = False
            for nm in infos:
                if(nm.split("-")[0] == "error"):
                    achou = True
                    break
            if(achou):
                print("Removendo pasta com erros: "+exp+"/"+tp+"/"+user)
                com_erro += 1
                if(delete):
                    shutil.rmtree("../processed/"+exp+"/"+tp+"/"+user)
                continue

print()
print()
print()
print("Pastas com numero de fotos incorreto: ", num_incorreto)
print("Pastas Vazias: ", pasta_vazia)
print("Pastas com erro: ", com_erro)
