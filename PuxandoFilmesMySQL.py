import PySimpleGUI as sg
import random
from arquivos import *
from dados import *
from main import *
from banco.conexão import *

##Inserção de filmes
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

d = dict()

sg.theme('DarkBlue1')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Olá! Bem vindo ao meu Projeto ChooseMovie.')],
            [sg.Text('Escolha o que deseja fazer clicando nos botões a baixo:')],
            [sg.Txt( key='-OUTPUT-')  ],
            [sg.Button('Aleatorizar'), sg.Button('Inserir'), sg.Button('Sair')] ]

# Create the Window
window = sg.Window('ChoseMovie', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Sair': # if user closes window or clicks cancel
        break
    
    elif event == 'Aleatorizar':
        con = CriarConexao("localhost", "root", "", "biblioteca")
        cursor = con.cursor()
        sql = "SELECT id,ano,filme FROM cinema"
        cursor.execute(sql)
        
        
        for (id,ano,filme) in cursor:
            d[id] = ano, filme

        tam = len(d.keys())

        try:

            ident = random.choice(list(d.items()))
            af = ident[1]
            ano = af[0]
            filme = af[1] 
        except:
            window['-OUTPUT-'].update('ERRO')
            continue
        window['-OUTPUT-'].update(f'O ano de lançamento é {ano} o filme escolhido foi {filme}.')
                 
            
    elif event == 'Inserir':
        
        sg.theme('DarkBlue1')   # Add a touch of color
        # All the stuff inside your window.
        layout = [  [sg.Text('Ano do Filme:  ', size=(13,1)), sg.InputText()],
                    [sg.Text('Nome do Filme: ', size=(13,1)), sg.InputText()],
                    [sg.Button('Adicionar'), sg.Button('Cancelar')] ]

        # Create the Window
        window = sg.Window('ChooseMovie', layout)
        # Event Loop to process "events" and get the "values" of the inputs
        while True:
            
            event, values = window.read()
            if event == sg.WIN_CLOSED : # if user closes window
                break
            
            elif event == 'Cancelar':   
                window.close()
                
            elif event == 'Adicionar':
                #Inserção de filmes
                con = CriarConexao("localhost", "root", "", "biblioteca")
                cursor = con.cursor()

                ano = values[0]
                filme = values[1]

                InserirFilme(con, ano, filme)

                FecharConexao

                sg.popup('O ano e filme inseridos foi: ', values[1], 'de', values[0])
                print('O Ano e Filme inseridos foi: Filme', values[1], 'de' , values[0])
                window.close()
                
window.close()

#_____________________________________________________________________________________________________________


    