
import os

import shutil

delete = input("Desseja deletar as inconsistencias detectadas? s/n   ")
delete = delete == "s" or delete == "S"
users_list = []
expressions = os.listdir("../processed")
for exp in expressions:
    types = os.listdir("../processed/"+exp)
    for tp in types:
        users = os.listdir("../processed/"+exp+"/"+tp)
        for user in users:
            infos = os.listdir("../processed/"+exp+"/"+tp+"/"+user)
            if(len(infos) == 0):
                if user not in users_list:
                    users_list.append(
                        [user, "Pasta vazia no "+exp+"/"+tp+"/"+user])
                continue

            if(len(infos) != 3):
                if user not in users_list:
                    users_list.append(
                        [user, "Pasta com " + str(len(infos)) + " imagens no " + exp+"/"+tp+"/"+user])
                continue
            achou = False
            for nm in infos:
                if(nm.split("-")[0] == "error"):
                    achou = True
                    break
            if(achou):
                if user not in users_list:
                    users_list.append(
                        [user, "Pasta com algum erro no " + exp+"/"+tp+"/"+user])
                continue
print()
print()
print("Excluindo pastas de " + str(len(users_list))+" users:")
for user in users_list:
    print(user)
print()

if(delete):
    for user in users_list:
        exps = ["00", "01", "02", "03", "04", "05", "06", "07"]
        tps = ["00", "01"]
        for exp in exps:
            for tp in tps:
                try:
                    print("excluindo "+exp+"/"+tp+"/"+user[0])
                    shutil.rmtree("../processed/"+exp+"/"+tp+"/"+user[0])
                except Exception as exception:
                    print("Erro ao excluir: " + str(exception))

            print()
