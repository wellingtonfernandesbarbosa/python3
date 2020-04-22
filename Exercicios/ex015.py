cor = {'limpa':   '\033[m',
       'verde':   '\033[32m',
       'amarelo': '\033[33m',
       'azul':    '\033[34m'}
d = int(input('Quantos dias alugados: '))
km = float(input('Quantos quilômetros rodados: '))
v = (d*60) + (km*0.15)
print('Um carro alugado por {}{}{} dias e com {}{}km{} percorridos terá o valor final do aluguel de {}R$ {:.2f}{}.'
      .format(cor['amarelo'], d, cor['limpa'], cor['verde'], km, cor['limpa'], cor['azul'], v, cor['limpa']))
