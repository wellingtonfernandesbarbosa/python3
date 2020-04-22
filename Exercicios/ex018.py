from math import radians, sin, cos, tan
from time import sleep
cor = {'verde': '\033[32m',
       'azul': '\033[34m',
       'lilás': '\033[35m',
       'amarelo': '\033[33m'}
n = float(input('{}Digite o ângulo que você deseja: '.format(cor['verde'])))
an = radians(n)
se = sin(an)
co = cos(an)
ta = tan(an)
print('{}O ângulo de {}º equivale aos valores: '.format(cor['azul'], n))
print('{}CALCULANDO...'.format(cor['amarelo']))
sleep(2)
print('{}Seno {:.2f} \nCosseno {:.2f} \nTangente {:.2f}'.format(cor['lilás'], se, co, ta))
