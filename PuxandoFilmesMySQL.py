import PySimpleGUI as sg
import random
from arquivos import *
from dados import *
from banco.DataFunctions import *
import banco.conexão


sg.theme('DarkBlue1')   # Tema da Janela

# O codigo da Interface dentro da Janela.
layout = [  [sg.Text('Olá! Bem vindo ao meu Projeto ChooseMovie.')],
            [sg.Text('Escolha o que deseja fazer clicando nos botões a baixo:')],
            [sg.Txt( key='-OUTPUT-')  ],
            [sg.Button('Aleatorizar'), sg.Button('Inserir'), sg.Button('Sair')] ]

# Criação da Janela
window = sg.Window('ChoseMovieMain', layout)

# Evento de Loop para processar "events" e pega os "values" das colocações.
while True:
    
    d = dict()
    
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'Sair': # Se o usuario fechar a Janela ou clicar em cancelar.
        break
    
    elif event == 'Aleatorizar': # Se o usuario Clicar no botão "Aleatorizar".

        # Fazendo conexão com o banco.
        con = CriarConexao("localhost", "root", "", "biblioteca")
        cursor = con.cursor()
        sql = "SELECT id,ano,filme FROM cinema"
        cursor.execute(sql)
        
        # Faz o id virar chave e ano e filme um item de um dicionario.
        for (id,ano,filme) in cursor:
            d[id] = ano, filme

        try:
            # Aleatoriza os itens como de acordo com o id
            ident = random.choice(list(d.items()))

            # Seleciona somente os itens
            af = ident[1]
            # Separa o primeiro item declarando-o como "ano"
            ano = af[0]
            # Separa o segundo item declarando-o como "filme"
            filme = af[1] 

        except:
            window['-OUTPUT-'].update('ERRO')
            continue
        
        # Caso de sucesso retornará os valores como de acordo.
        window['-OUTPUT-'].update(f'O ano de lançamento é {ano} o filme escolhido foi {filme}.')
                    
    elif event == 'Inserir': # Se o usuario Clicar no botão "Inserir".
        
        sg.theme('DarkBlue')
        # Caixas de texto para colocar o ano e o filme respectivamente. 
        layout = [  [sg.Text('Ano do Filme:  ', size=(13,1)), sg.InputText()],
                    [sg.Text('Nome do Filme: ', size=(13,1)), sg.InputText()],
                    [sg.Button('Adicionar'), sg.Button('Cancelar')]]
        window = sg.Window('ChooseMovieInserir', layout)
        
        while True:
            
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancelar':
                break
                
            #Inserção de filmes    
            elif event == 'Adicionar': # Se o usuario Clicar no botão "Adicionar".
                
                # Conexão com o banco
                con = CriarConexao("localhost", "root", "", "biblioteca")
                cursor = con.cursor()
                #Associando os valores adicionados as caixas de texto as variaveis.
                ano = values[0]
                filme = values[1]
                InserirFilme(con, ano, filme)
                FecharConexao
                sg.popup('O ano e filme inseridos foi: ', values[1], 'de', values[0])
                print('O Ano e Filme inseridos foi: Filme', values[1], 'de' , values[0])
        window.close()
                
window.close()
                



    