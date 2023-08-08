import csv

with open('arquivos/Filmes.csv','r') as arquivo:
    leitor = csv.reader(arquivo)
    dados = list(leitor)

    print(dados)