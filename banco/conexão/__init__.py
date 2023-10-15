import mysql.connector

def CriarConexao(host, usuario,senha,banco):

    """
    CriarConexao → Conecta ao banco de dados.
    
    Parâmetros:
        - Host, usuario, senha, database.
        
    Retorna:
        - Retornara sucesso à conexão.
        - Retornara uma mensagem de erro caso os parametros não sejam atendidos.

    """
    
    try:
        conectado = mysql.connector.connect(host=host, user=usuario, password=senha, database=banco) 
    except mysql.connector.Error:
        print('Erro ao tentar se conectar')
    else:
        return conectado
    
    
    
def FecharConexao(con):

    """
    FecharConexao → Fecha conexão com o banco de dados.
    
    Parâmetros:
        - Conexão.
        
    Retorna:
        - Retornará o fechamento do banco.
        - Não retornará nada.

    """

    con.close()