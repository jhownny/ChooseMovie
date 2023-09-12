from persona import *
import csv
import random

def ArqExiste(nome):
    
    """
    ArqExiste → Verifica a existencia do arquivo.
    
    Parâmetros:
        - Caminho do arquivo
        
    Retorna:
        - Retornara True caso o arquivo exista.
        - Retornara Falso caso o arquivo não exista.
        
    """
    
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else: 
        return True
    
    
def CriarArq(nome):
    
    """
    CriarArq → Cria um arquivo.
    
    Parâmetros:
        - Caminho do arquivo a ser adicionado    

    Retorna:
        - Retorna mensagem de sucesso caso consiga criar o arquivo.
        - Retorna mensagem de erro caso não consiga criar o arquivo.
        
    """
    
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Ocorreu um ERRO ao criar o arquivo')
    else:
        print(f'Aquivo {nome} criado com sucesso!')
        

def LerArq(nome):
    
    """
    LerArq → ler um arquivo.
    
    Parâmetros:
        - Caminho do arquivo a ser lido   

    Retorna:
        - Retorna mensagem de sucesso caso consiga criar o arquivo.
        - Retorna mensagem de erro caso não consiga criar o arquivo.
        
    """
    
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo')
    else:
        linhazinha()
        LetraCor('      PESSOAS CADASTRADAS',3,1)
        linhazinha()
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()
    

def cadastrar(arq, nome='desconhecido', idade= 0):
    
    """
    CADASTRAR → Cadastrar pessoas.
    
    Parâmetros:
        - Caminho do arquivo a que será inserido o cadastro.  
        - Nome a ser cadastrado.
        - Idade a ser cadastrada.

    Retorna:
        - Retorna mensagem de sucesso caso consiga cadastrar.
        - Retorna mensagem de erro caso não consiga cadastrar.
        
    """
    
    try:
        a = open(arq,'at')
    except:
        print('Ocorreu um erro na abertura do aquivo!')
    else:
        try:
            a.write(f'{nome.title()};{idade}')
        except:
            print('Ocorreu um erro na escritura do arquivo!')
        else:
            print(f'Novo registro de {nome} adicionado.\n')
            a.close()

            
# Função para carregar os dados do arquivo CSV para um dicionário
def carregar_filmes(filename):
    filmes = {}
    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                ano, filme = row
                filmes[ano] = filme
    except FileNotFoundError:
        pass
    return filmes

# Função para salvar os dados do dicionário em um arquivo CSV
def salvar_filmes(filename, filmes):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for ano, filme in sorted(filmes.items()):
            writer.writerow([ano, filme])

# Função para escolher aleatoriamente um filme e ano
def escolher_aleatoriamente(filmes):
    if filmes:
        ano, filme = random.choice(list(filmes.items()))
        return f'Ano: {ano}, Filme: {filme}'
    else:
        return 'Não há filmes registrados.'    
        