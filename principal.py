import PySimpleGUI as sg
import random
import csv
from arquivos import *
from dados import *

path = "arquivos/Filmes.csv"

if not ArqExiste(path):
    CriarArq(path)


#(Escolhendo Aleatorio Filme - Dicionario)

with open('arquivos/Filmes.csv','r') as arquivo:
    leitor = csv.reader(arquivo)
    ano = list(leitor)
    ql = len(ano)
    fl = random.randrange(1, ql-1)
    al = random.randrange(0, 4)

#eafd = {'1960':['The Great Escape', 'What Ever Happened to Baby Jane?', 'For a Few Dollars More', 'Night of the Living Dead', 'Psycho', 'Harakiri', 'The Good, the Bad and the Ugly', 'Eyes Without a Face']
#    , '1970':['Alien', 'Blazing Saddles', 'Taxi Driver', 'The Godfather', 'Stalker', 'Jaws', 'The Exorcist', 'A Clockwork Orange']
#    , '1980':['Beetlejuice', 'An American Werewolf in London', 'The Thing', 'Scarface', 'The Color Purple', 'The Shining', 'Apocalypse Now', 'Once Upon a Time in America']
#    , '1990':['Malcolm X', 'Se7en', 'Heat', 'The Devils Advocate', 'Perfect Blue', 'Misery', 'Schindlers List', 'GoodFellas']
#    , '2000':['Office Space', 'No Country for Old Men', 'Watchmen', 'Who Am I', 'The Conjuring', 'Into the Wild', 'The Imitation Game', 'Get Out']}

#layout
sg.theme('LightBrown13')
layout = [
    [sg.Text(f'O Ano escolhido foi {ano[0][al]} e o Filme escolhido foi {ano[fl][al]}')]
]

# Janela
janela = sg.Window('Escolhendo Filmes', layout)

# Ler os Eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break

