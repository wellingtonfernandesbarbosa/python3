from lib.interface import *
from time import sleep


def arquivoExiste(msg):
    try:
        file = open(msg)
    except FileNotFoundError:
        print(f'O arquivo não {msg} não existe.')
    else:
        print(f'Arquivo {msg} encontrado com sucesso!')
    finally:
        file.close()


def cadastro(texto, nome='Desconhecido', idade='0'):
    try:
        texto = open('texto.txt', 'a')
    except:
        print(f'O arquivo {texto} não pode ser aberto.')
    else:
        nome = input('Nome: ')
        idade = input('Idade: ')
        texto.write(f'{nome};{idade}' + '\n')
    finally:
        texto.close()


def lerArquivo(msg):
    try:
        arquivo = open(msg, 'rt')
    except:
        print(f'Não foi possível abrir o arquivo {msg}')
    else:
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<33}{dado[1]:>3} anos')
    finally:
        arquivo.close()
