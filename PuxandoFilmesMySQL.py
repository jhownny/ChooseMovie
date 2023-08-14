import PySimpleGUI as sg
import random
import pandas as pd
import csv
from arquivos import *
from dados import *
from main import *
from banco.conexão import *

# Inserção de filmes
#con = CriarConexao("localhost", "root", "", "biblioteca")
#cursor = con.cursor()
#
#ano = input('Digite o ano do filme: ')
#filme = input('Digite o nome do filme: ')
#
#InserirFilme(con, ano, filme)
#MostrarFilmes(con)
#
#FecharConexao
#
#con = CriarConexao("localhost", "root", "", "biblioteca")
#cursor = con.cursor()
#sql = "SELECT id,ano,filme FROM cinema"
#cursor.execute(sql)
#    
#for (id,ano,filme)in cursor:
#    print(id,ano,filme)
#    
#cursor.close()
#
#
#con = CriarConexao("localhost", "root", "", "biblioteca")
#cursor = con.cursor()
#sql = "SELECT id,ano,filme FROM cinema"
#cursor.execute(sql)
#for (ano,filme)in cursor:
#    print('hfdighsauidfhi')
#cursor.close()

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Digite o ano do filme: '), sg.InputText()],
            [sg.Text('Digite o nome do filme: '), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('ChooseMovie', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered: ', values[0], 'and' , values[1])