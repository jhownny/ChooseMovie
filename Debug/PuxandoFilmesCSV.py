import PySimpleGUI as sg
import random
import pandas as pd
import csv
from arquivos import *
from dados import *


#with open('arquivos/Filmes.csv', newline='') as arquivo:
#    reader = csv.DictReader(arquivo)
#    for row in reader:
#        print(row['1960'], row['1970'])       
#    print(row)
#-------------------------------------------

df = pd.read_csv('arquivos/Filmes.csv')

print(df)

pd.DataFrame(5,'a','coluna')

#------------------------------
#ano = str(input('Informe o ano do filme: '))
#filme = str(input('Informe o nome do filme:'))
#with open("arquivos/Filmes.csv", "a+") as arquivo:
#    #arquivo.write(cinema)
#    fieldnames = [ano]
#    writer = csv.DictWriter(arquivo, fieldnames=fieldnames)
#    
#    writer.writeheader()
#    writer.writerow({ano: filme})
#___________________________________
#cinema = csv.DictWriter(ano,filme)
#linha = str(ano)+","+str(filme)
#------------------------------------
    
    
    
    
#---------------------------------------   
#with open('arquivos/Filmes.csv','r') as arquivo:
#    leitor = csv.reader(arquivo)
#    ano = list(leitor)
#    ql = len(ano)
#    fl = random.randrange(1, ql-1)
#    al = random.randrange(0, 4)
#----------------------------------------- 

   
   
##layout
#sg.theme('LightBrown13')
#layout = [
#     [sg.Text(f'O Ano escolhido foi {ano[0][al]} e o Filme escolhido foi{ano[fl][al]}')]
#]
#
## Janela
#janela = sg.Window('Escolhendo Filmes', layout)
#
## Ler os Eventos
#while True:
#    eventos, valores = janela.read()
#    if eventos == sg.WINDOW_CLOSED:
#        break
#    