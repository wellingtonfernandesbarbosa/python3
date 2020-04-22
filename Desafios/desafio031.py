print('Calculadora de passagem')
d = int(input('Qual a distância da viagem? '))
if d <= 200:
    print('O valor da passagem será de R${:.2f}'.format(d * 0.5))
else:
    print('O valor da passagem será de R${:.2f}'.format(d * 0.45))
