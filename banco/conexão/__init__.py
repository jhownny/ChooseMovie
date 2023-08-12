from mysql.connector import *

def CriarConexao(host, usuario,senha,banco):
    try:
        conectado = connect(host=host, user=usuario, password=senha, database=banco) 
    except:
        print('Erro ao tentar se conectar')
    else:
        return conectado
    
    
    
def FecharConexao(con):
    con.close()