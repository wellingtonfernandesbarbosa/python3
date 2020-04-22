from random import choice
cor = {'azulb': '\033[36m',
       'verde': '\033[32m'}
n1 = str(input('{}Nome do primeiro aluno: '.format(cor['azulb'])))
n2 = str(input('Nome do segundo aluno: '))
n3 = str(input('Nome do terceiro aluno: '))
n4 = str(input('Nobre do quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('{}O aluno escolhido foi {}'.format(cor['verde'], escolhido))
