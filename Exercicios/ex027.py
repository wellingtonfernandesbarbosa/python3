print('{}='.format('\033[35m') * 48)
print('              Analizador de nomes')
print('=' * 48)
n = str(input('{}Digite seu nome completo: '.format('\033[33m'))).strip().title()
print('{}Muito prazer em te conhecer {}.'.format('\033[34m', n))
nome = n.split()
u = len(nome)-1
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[u]))
