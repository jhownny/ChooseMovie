from mysql.connector import *

def CriarConexao(host, usuario, senha, banco):
    return connect(host=host, user=usuario, password=senha, database=banco)

def FecharConexao(con):
    return con.close()