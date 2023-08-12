import PySimpleGUI as sg
import random
import pandas as pd
import csv
from arquivos import *
from dados import *
from main import *

main()



##layout
#sg.theme('LightBrown13')
#layout = [
#     [sg.Text(f'O Ano escolhido foi {ano[0][al]} e o Filme escolhido foi{ano[fl][al]}')]
#]
##
## Janela
#janela = sg.Window('Escolhendo Filmes', layout)
##
## Ler os Eventos
#while True:
#    eventos, valores = janela.read()
#    if eventos == sg.WINDOW_CLOSED:
#        break
#    