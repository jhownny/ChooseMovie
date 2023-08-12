import pandas as pd
import random
import csv
from arquivos import *
from dados import *

arq = "arquivos/temporario.csv"

if not ArqExiste(arq):
    CriarArq(arq)
    
    
ano = int(input('Informe o ano do filme: '))
filme = str(input('Informe o nome do filme:'))
with open("arquivos/temporario.csv", "a+", newline='') as arquivo:
    #arquivo.write(cinema)
    fieldnames = [ano]
    writer = csv.DictWriter(arquivo, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerow({ano: filme})
    

with open('arquivos/temporario.csv','r') as arquivo:
    leitor = csv.reader(arquivo)
    ano = list(leitor)
    ql = len(ano)
    fl = random.randrange(1, ql-1)
    al = random.randrange(1)

print(f'{ano}')


df = pd.read_csv('arquivos/Filmes.csv')
#
#print(df)
#
df2 = pd.read_csv('arquivos/temporario.csv')
#
#print(df2)

#concat = pd.concat([df,df2],verify_integrity=True, axis=1, ignore_index=False)
#print(concat)
#
#print('\n-----------+++++++++++++++++++++++++++++++++++++++++++++-----------\n')
#
#join = df.join(df2)
#print(join)
