
import os

import shutil
from definitions import *

delete = input(
    "SÓ EXECUTA COM O SIM SE VC JA TERMINOU O ANALYSER!!!!!!!!!!\nDesseja deletar as inconsistencias detectadas? s/n   ")
delete = delete == "s" or delete == "S"
users_list = [[], []]
expressions = os.listdir(PROCESSED_PATH)


def checkIn(num, lista):  # o not in não funciona...
    achou_igual = False
    for item in lista:
        if(int(item) == int(num)):
            achou_igual = True
            break

    return achou_igual


for exp in expressions:
    if(len(exp.split(".")) > 1):
        continue
    types = os.listdir(PROCESSED_PATH + "/"+exp)
    for tp in types:
        if(len(tp.split(".")) > 1):
            continue
        users = os.listdir(PROCESSED_PATH + "/"+exp+"/"+tp)
        for user in users:
            if(len(user.split(".")) > 1):
                continue
            infos = os.listdir(PROCESSED_PATH + "/"+exp+"/"+tp+"/"+user)
            arqs = []
            for arq in infos:
                if(arq.split(".")[1] == "csv"):
                    arqs.append(arq)
            if(len(arqs) == 0):
                if not checkIn(user, users_list[0]):
                    users_list[0].append(
                        int(user))
                    users_list[1].append("Pasta vazia no "+exp+"/"+tp+"/"+user)

                continue

            if(len(arqs) != 4):
                if not checkIn(user, users_list[0]):
                    users_list[0].append(
                        int(user))
                    users_list[1].append(
                        "Pasta com " + str(len(arqs)) + " imagens no " + exp+"/"+tp+"/"+user)
                continue
            achou = False
            for nm in arqs:
                if(nm.split("-")[0] == "error"):
                    achou = True
                    break
            if(achou):
                if not checkIn(user, users_list[0]):
                    users_list[0].append(
                        int(user))
                    users_list[1].append(
                        "Pasta com algum erro no " + exp+"/"+tp+"/"+user)

                continue
print()
print()
print("Excluindo pastas de " + str(len(users_list[0]))+" users:")
for i, user in enumerate(users_list[0]):
    print(user, users_list[1][i])
print()

if(delete):
    for user in users_list[0]:
        exps = ["00", "01", "02", "03", "04", "05", "06", "07"]
        tps = ["00", "01"]
        for exp in exps:
            for tp in tps:
                try:
                    shutil.rmtree(PROCESSED_PATH + "/"+exp +
                                  "/"+tp+"/"+str(user[0]))
                except Exception as exception:
                    continue

            print()
