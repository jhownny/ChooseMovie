from banco.conexão import *

def InserirFilme(con, ano, filme):
    cursor = con.cursor()
    sql = "INSERT INTO cinema (ano, filme) values(%s, %s)"
    valores = (ano, filme)
    cursor.execute(sql,valores)
    cursor.close()
    con.commit()
    
    
def MostrarFilmes(con):
    cursor = con.cursor()
    sql = "SELECT id,ano,filme FROM cinema"
    cursor.execute(sql)
    
    for (id,ano,filme)in cursor:
        print(id,ano,filme)
        
    cursor.close()
    
    
def main():
    con = CriarConexao("localhost", "root", "", "biblioteca")
    
    #InserirFilme(con, "2022", "Tudo em Todo o Lugar ao Mesmo Tempo")
    MostrarFilmes(con)
    
    FecharConexao


            
            