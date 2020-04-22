from lib.interface import *
from time import sleep

def arquivoExiste(msg):
    try:
        file = open(msg, 'r')
    except FileNotFoundError:
        print(f'O arquivo não {msg} não existe.')
        file = open(msg, 'w')
        print(f'Arquivo {msg} criado com sucesso.')
    else:
        print(f'Arquivo {msg} encontrado com sucesso!')
    finally:
        file.close()


def cadastro(texto, nome='Desconhecido', idade=0):
	try:
		texto = open('texto.txt', 'a')
	except:
		print(f'O arquivo {texto} não pode ser aberto.')
	else:
		nome = input('Nome: ')
		idade = input('Idade: ')
		texto.write(f'{nome};{idade}' + '\n')
		print(f'Cadastro de {nome} criado com sucesso.')
	finally:
		texto.close()


def lerArquivo(msg):
	try:
		file = open(msg, 'rt')
		sleep(0.4)
	except:
		print(f'Não foi possível abrir o arquivo {msg}')
	else:
		cabeçalho('LISTAR PESSOAS')
		sleep(0.4)
		for linha in file:
			dado = linha.split(';')
			dado[1] = dado[1].replace('\n', '')
			print(f'{dado[0]:<33}{dado[1]:>3} anos')
			sleep(0.4)
	finally:
		file.close()
