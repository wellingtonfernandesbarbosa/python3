from lib.interface import *
from lib.arquivo import *
from time import sleep

file = 'texto.txt'
teste = arquivoExiste(file)
cabeçalho('TESTE')
while True:
    res = menu(['Listar Pessoas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    sleep(1)
    if res == 1:
        lerArquivo(file)
    elif res == 2:
        cadastro(file)
    elif res == 3:
        cabeçalho('Saindo do sistema... Até logo')
        break
    else:
        print('\033[31mERRO! Por favor digite uma opção válida!\033[m')
