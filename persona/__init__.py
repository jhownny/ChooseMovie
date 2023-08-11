def LetraCor(texto, cor, est):
    
    """
    
    LETRACOR -> Permite o usuraio personalizar/mudar o estilo da escrita permitindo traca de cor e estilização
    
    Padrão:
        - Texto: Escrito pelo Proprio Usuario.
        - Cor: (0 = 'nulo'), 
            (1 = 'branco'),
            (2 = 'vermelho'),
            (3 = 'verde'),
            (4 = 'amarelo'),
            (5 = 'azul'),
            (6 = 'roxo'),
            (7 = 'ciano'),
            (8 = 'cinza').
            
        - Estilização: (0 = 'nulo'), 
            (1 = 'negrito'),
            (2 = 'linha'),
            (3 = 'negativo').
    
    Parâmetro:
        - Inserção do Texto a ser Personalizado.
        - Inserção da Cor para Personalização.
        - Inserção da Estilização para Personalização.
        
    Retorna:
        - Texto[str] estilizado como de acordo com os valores inseridos.
        
    """

    if cor == 1 or cor == 'branco':
        if est == 'nulo' or est == 0:
            print(f'\033[0;30m{texto}\033[m')
        elif est == 'negrito' or est == 1:
            print(f'\033[1;30m{texto}\033[m')
        elif est == 'linha' or est == 2:
            print(f'\033[4;30m{texto}\033[m')
        elif est == 'negativo' or est == 3:
            print(f'\033[7;30m{texto}\033[m')

    elif cor == 2 or cor == 'vermelho':
        if est == 'nulo' or est == 0:
            print(f'\033[0;31m{texto}\033[m')
        elif est == 'negrito' or est == 1:
            print(f'\033[1;31m{texto}\033[m')
        elif est == 'linha' or est == 2:
            print(f'\033[4;31m{texto}\033[m')
        elif est == 'negativo' or est == 3:
            print(f'\033[7;31m{texto}\033[m')

    elif cor == 3 or cor == 'verde':
        if est == 'nulo' or est == 0:
            print(f'\033[0;32m{texto}\033[m')
        elif est == 'negrito' or est == 1:
            print(f'\033[1;32m{texto}\033[m')
        elif est == 'linha' or est == 2:
            print(f'\033[4;32m{texto}\033[m')
        elif est == 'negativo' or est == 3:
            print(f'\033[7;32m{texto}\033[m')

    elif cor == 4 or cor == 'amarelo':
        if est == 'nulo' or est == 0:
            print(f'\033[0;33m{texto}\033[m')
        elif est == 'negrito' or est == 1:
            print(f'\033[1;33m{texto}\033[m')
        elif est == 'linha' or est == 2:
            print(f'\033[4;33m{texto}\033[m')
        elif est == 'negativo' or est == 3:
            print(f'\033[7;33m{texto}\033[m')

    elif cor == 5 or cor == 'azul':
        if est == 'nulo' or est == 0:
            print(f'\033[0;34m{texto}\033[m')
        elif est == 'negrito' or est == 1:
            print(f'\033[1;34m{texto}\033[m')
        elif est == 'linha' or est == 2:
            print(f'\033[4;34m{texto}\033[m')
        elif est == 'negativo' or est == 3:
            print(f'\033[7;34m{texto}\033[m')  

    elif cor == 6 or cor == 'roxo':
        if est == 'nulo' or est == 0:
            print(f'\033[0;35m{texto}\033[m')
        elif est == 'negrito' or est == 1:
            print(f'\033[1;35m{texto}\033[m')
        elif est == 'linha' or est == 2:
            print(f'\033[4;35m{texto}\033[m')
        elif est == 'negativo' or est == 3:
            print(f'\033[7;35m{texto}\033[m')

    elif cor == 7 or cor == 'ciano':
        if est == 'nulo' or est == 0:
            print(f'\033[0;36m{texto}\033[m')
        elif est == 'negrito' or est == 1:
            print(f'\033[1;36m{texto}\033[m')
        elif est == 'linha' or est == 2:
            print(f'\033[4;36m{texto}\033[m')
        elif est == 'negativo' or est == 3:
            print(f'\033[7;36m{texto}\033[m')

    elif cor == 8 or cor == 'cinza':
        if est == 'nulo' or est == 0:
            print(f'\033[0;37m{texto}\033[m')
        elif est == 'negrito' or est == 1:
            print(f'\033[1;37m{texto}\033[m')
        elif est == 'linha' or est == 2:
            print(f'\033[4;37m{texto}\033[m')
        elif est == 'negativo' or est == 3:
            print(f'\033[7;37m{texto}\033[m')

    else: 
        if est == 'negrito' or est == 1:
            print(f'\033[1m{texto}\033[m')
        elif est == 'linha' or est == 2:
            print(f'\033[4m{texto}\033[m')
        elif est == 'negativo' or est == 3:
            print(f'\033[7m{texto}\033[m')
        else:
            print(f'\033[0m{texto}\033[m')
 
   
def linhazinha():

    print('-' * 30) 

    