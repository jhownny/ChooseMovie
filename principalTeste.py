import csv
from random import randrange

with open('arquivos/Filmes.csv','r') as arquivo:
    leitor = csv.reader(arquivo)
    ano = list(leitor)
    ql = len(ano)
    fl = randrange(1, ql-1)
    al = randrange(0, 4)
    
    print(f'O ano escolhido foi \033[1;32m{ano[0][al]}\033[m e o filme \033[1;36m{ano[fl][al]}\033[m.')
