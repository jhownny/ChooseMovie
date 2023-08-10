import csv
from random import randrange
from conexão import CriarConexao, FecharConexao

def InserirFilmes(con,ano,filme):
    cursor = con.cursor()
    sql = "INSERT INTO filmes (ano, filme) values (%s, %s, %s)"
    valores = (ano, filme)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()

def MostrarFilmes(con):
    cursor = con.cursor()
    sql = "SELECT id, ano, filme FROM cinema"
    cursor.execute(sql)
    
    for (id, ano, filme) in cursor:
        print(id, ano, filme)
    
    cursor.close()

def main():
    con = CriarConexao("localhost", "ano", "filmes",)
    
    InserirFilmes(con, "2022", "Tudo em Todo Lugar ao Mesmo Tempo")
    MostrarFilmes(con)
    
    FecharConexao(con)

with open('arquivos/Filmes.csv','r') as arquivo:
    leitor = csv.reader(arquivo)
    ano = list(leitor)
    ql = len(ano)
    fl = randrange(1, ql-1)
    al = randrange(0, 4)
    
    print(f'O ano escolhido foi \033[1;32m{ano[0][al]}\033[m e o filme \033[1;36m{ano[fl][al]}\033[m.')
