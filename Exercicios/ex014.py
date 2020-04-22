cor = {'limpa': '\033[m',
       'azul':  '\033[34m',
       'verde': '\033[32m'}
c = float(input('Informe a temperatura em ºC: '))
f = ((9*c)/5) + 32
print('A temperatura de {}{}ºC{} corresponde a {}{:.2f}ºF{}.'
      .format(cor['verde'], c, cor['limpa'], cor['azul'], f, cor['limpa']))
