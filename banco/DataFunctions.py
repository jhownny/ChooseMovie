from conexão import *

def InserirFilme(con, ano, filme):

    """
    InserirFilme → Conecta ao banco de dados e Insere ano e filmes .
    
    Parâmetros:
        - Conexão, ano e Filme a ser inseridos.
        
    Retorna:
        - Retornara resultados ao banco caso tenha sucesso na adição.
        - Não retornara nada ao banco caso não tenha sucesso na adição.

    """
    try:
        cursor = con.cursor()
        sql = "INSERT INTO cinema (ano, filme) values(%s, %s)"
        valores = (ano, filme)
        cursor.execute(sql,valores)
        cursor.close()
        con.commit()
        
    except Exception as erro:
        print(f'Ocorreu o erro {erro.__class__} ao tentar se conectar ao Banco de Dados.')

    else:
        return
    
    finally:
        print('Conexão bem sucedida!')
    
def MostrarFilmes(con):

    """
    MostrarFilmes → Verifica a existencia do arquivo.
    
    Parâmetros:
        - Caminho do arquivo
        
    Retorna:
        - Retornara True caso o arquivo exista.
        - Retornara Falso caso o arquivo não exista.
        
    """

    cursor = con.cursor()
    sql = "SELECT id,ano,filme FROM cinema"
    cursor.execute(sql)
    
    for (id,ano,filme)in cursor:
        print(id,ano,filme)
        
    cursor.close()
    
    
def main():
    con = CriarConexao("localhost", "root", "", "biblioteca")
    
    InserirFilme(con, "2022", "Tudo em Todo o Lugar ao Mesmo Tempo")
    MostrarFilmes(con)
    
    FecharConexao


            
            