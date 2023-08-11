import PySimpleGUI as sg
import random
import csv
from arquivos import *
from dados import *

with open('arquivos/Filmes.csv','r') as arquivo:
    leitor = csv.reader(arquivo)
    ano = list(leitor)
    ql = len(ano)
    fl = random.randrange(1, ql-1)
    al = random.randrange(0, 4)
    
#layout
sg.theme('LightBrown13')
layout = [
     [sg.Text(f'O Ano escolhido foi {ano[0][al]} e o Filme escolhido foi{ano[fl][al]}')]
]

# Janela
janela = sg.Window('Escolhendo Filmes', layout)

# Ler os Eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    