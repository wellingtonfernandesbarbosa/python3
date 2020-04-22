cor = {'amarelo': '\033[33m',
       'azulc': '\033[36m'}
nome = str(input('{}Qual o seu nome completo? '.format(cor['amarelo']))).title()
print('{}O seu nome tem Silva? {}'.format(cor['azulc'], 'Silva' in nome))
