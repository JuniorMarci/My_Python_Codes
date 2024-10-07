from math import floor
from time import sleep
from datetime import datetime as dt
from os import listdir as ld, rmdir, rename, makedirs
import psycopg2
import pandas
import pickle

#rmdir("d-1")
#rename("d",'d-1')
pre = "C:\\Outliers\\"
d = pre+str(dt.now())[:10]
if(d.split('\\')[-1] not in ld(pre)): makedirs(d)

with open(r"C:\Chave.pkl", 'rb') as file: k = pickle.load(file)



def conectar():

    # Connect to your PostgreSQL database
    connection = psycopg2.connect(
            host=k['db_address'],
            user=k['db_user'],
            password=k['db_password'],
            dbname=k['db_name']
        )

        # Create a cursor object
    cursor = connection.cursor()

    return cursor



c1 = conectar()

c1.execute(
f'''
SELECT distinct id
FROM table5
''')

ii = c1.fetchall()

c1.close()

def Baixar(ii,p,cursor):
    global d
    for c in ii:
        if(f'{str(c)}.parquet' in ld(d)): print(p,c,'já existe')#0==0
        else:


            sleep(0.05)
            cursor.execute(
                f'''
                SELECT *
                FROM table5
                where dataindice>='2022-01-07' and id={str(c)} and dataindice<='2024-01-09';
                ''')

            res = cursor.fetchall()
            cols = [c[0] for c in cursor.description]
            tab = pandas.DataFrame(res, columns=cols).drop_duplicates()
            tab.to_parquet(f'{d}/{str(c)}.parquet')

            print(p,c)

ii = sorted(ii)
nii= pandas.DataFrame(ii)
nii = nii[0].astype('str')+'.parquet'
nii = nii[~nii.isin(ld(d))]
ii = nii.str.replace(".parquet",'').astype('int')


t1 = dt.now()

qnt=5
divs = []

if(len(ii)%qnt>0):
    passo = int(floor(len(ii)/qnt))
    divs.append(ii[passo*qnt-len(ii):])
else: passo = int(len(ii)/qnt)

for g in range(0,qnt): divs.append(ii[passo*(g):passo*(g+1)])


print("Iniciado!",ii)


import threading as th
processos = []
for g in range(len(divs)):
    c = conectar()
    t = th.Thread(target=Baixar, args=(divs[g],g,c)) # Criar e iniciar a thread para a interface gráfica
    t.start()
    processos.append([t,c])

for g in processos:
    g[0].join()
    g[1].close()


    t2 = dt.now()
    print(f'Base completa extraída em {t2-t1}')