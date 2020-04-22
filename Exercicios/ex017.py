from math import hypot
from time import sleep
cor = {'limpa': '\033[m',
       'azul': '\033[34m',
       'azulb': '\033[36m',
       'amarelo': '\033[33m'}
print('{}-=-'.format(cor['azul']) * 12)
print('       Calculo da Hipotenusa')
print('-=-' * 12)
co = float(input('{}Digite o valor do cateto oposto: '.format(cor['azulb'])))
ca = float(input('Digite o valor do cateto adjacente: {}'.format(cor['limpa'])))
hi = hypot(co, ca)
print('{}CALCULANDO...'.format(cor['amarelo']))
sleep(2)
print('{}O valor da hipotenusa é {:.2f}.'.format(cor['azul'], hi))
