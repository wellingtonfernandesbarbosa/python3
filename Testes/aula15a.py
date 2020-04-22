nome = 'Wellington'
idade = 27
salario = 1224
print(f'{nome} tem {idade} anos e recebe R$ {salario:.2f}.')  #Python 3.6+
print('{} tem {} anos e recebe R$ {:.2f}.'.format(nome, idade, salario))  #Python 3
print('%s tem %d anos e recebe R$ %d.' % (nome, idade, salario))  #Python 2
