from time import sleep
from lib.interface import *

def arquivoExiste(msg):
    try:
        arquivo = open(msg)
        arquivo.close()
    except FileNotFoundError:
        print(f'Arquivo "{msg}" não existe.')
    else:
        print(f'Arquivo "{msg}" encontrado com sucesso')


def criarArquivo(msg):
    try:
        arquivo = open('texto.txt', 'wt+')
        arquivo.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {msg} criado com sucesso.')


def lerArquivo(msg):
    cabeçalho('PESSOAS CADASTRADAS')
    try:
        arquivo = open(msg, 'rt')
    except (FileNotFoundError, FileExistsError):
        print(f'Erro ao ler o arquivo "{msg}"')
    else:
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<34}{dado[1]:>3} anos')
            sleep(0.5)
    finally:
        arquivo.close()

def cadastrar(arquivo, nome='Desconhecido', idade='0'):
    try:
        arquivo = open(arquivo, 'at')
    except:
        print('Houve erro na abertura do arquivo')
    else:
        try:
            arquivo.write(f'{nome};{idade}\n')
        except:
            print('Houve erro na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} foi adicionado.')
            arquivo.close()
