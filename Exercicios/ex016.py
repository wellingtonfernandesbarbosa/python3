from math import trunc
cor = {'limpa': '\033[m',
       'azul': '\033[34m',
       'azulb': '\033[36m'}
n = float(input('Digite um número: '))
i = trunc(n)
print('O número {}{:.3f}{} tem a parte inteira {}{}{}'
      .format(cor['azulb'], n, cor['limpa'], cor['azul'], i, cor['limpa']))
