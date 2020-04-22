from lib.interface import *
from lib.arquivo import *
from time import sleep

lista = 'texto.txt'
arquivoExiste(lista)
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        lerArquivo(lista)
    elif resposta == 2:
        nome = input('Nome: ')
        idade = input('Idade: ')
        cadastrar(lista, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1)
