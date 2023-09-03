import PySimpleGUI as sg
import random
import pandas as pd
import csv
#from arquivos import *
#from dados import *




# Nome do arquivo CSV
nome_arquivo = 'arquivos/Filmes.csv'

# Função para ler os filmes do arquivo CSV e retornar um dicionário de anos e filmes
def ler_filmes():
    try:
        with open(nome_arquivo, 'r', newline='') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)
            filmes = {row['Ano']: row['Filmes'].split(', ') for row in leitor_csv}
    except FileNotFoundError:
        filmes = {}
    return filmes

# Função para adicionar (ano e filme) à lista existente de filmes
def adicionar_filme(filmes):
    novo_ano = input("Digite o ano do filme: ")
    novo_filme = input("Digite o nome do filme: ")

    # Verifique se o ano já existe nas chaves do dicionário de filmes
    if novo_ano in filmes:
        if novo_filme not in filmes[novo_ano]:
            filmes[novo_ano].append(novo_filme)
            print(f"Filme '{novo_filme}' do ano {novo_ano} adicionado à lista de filmes.")
        else:
            print(f"O filme '{novo_filme}' do ano {novo_ano} já existe na lista de filmes.")
    else:
        filmes[novo_ano] = [novo_filme]
        print(f"Filme '{novo_filme}' do ano {novo_ano} adicionado à lista de filmes.")

# Função para salvar a lista de filmes ordenada em um arquivo CSV
def salvar_filmes(filmes):
    with open(nome_arquivo, 'w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerow(['Ano', 'Filmes'])
        for ano, lista_filmes in sorted(filmes.items(), key=lambda x: int(x[0])):
            escritor_csv.writerow([ano, ', '.join(lista_filmes)])
        print("Filmes salvos no arquivo CSV.")

# Função principal
def main():
    filmes = ler_filmes()

    while True:
        print("\nMenu:")
        print("1. Adicionar um novo filme")
        print("2. Exibir filmes por ano")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_filme(filmes)
        elif opcao == '2':
            for ano, lista_filmes in sorted(filmes.items(), key=lambda x: int(x[0])):
                print(f"Ano: {ano}, Filmes: {', '.join(lista_filmes)}")
        elif opcao == '3':
            salvar_filmes(filmes)
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()




#with open('arquivos/Filmes.csv', newline='') as arquivo:
#    reader = csv.DictReader(arquivo)
#    for row in reader:
#        print(row['1960'], row['1970'])       
#    print(row)
#-------------------------------------------

#df = pd.read_csv('arquivos/Filmes.csv')
#
#print(df)
#
#pd.DataFrame(5,'a','coluna')

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