from random import shuffle
n1 = str(input('{}Digite o nome do primeiro aluno: '.format('\033[36m')))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('{}A ordem de apresentação será: {}{}'.format('\033[32m', '\033[1;35m', lista))
