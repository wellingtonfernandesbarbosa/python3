print('{}='.format('\033[34m') * 52)
print(' ' * 17, 'Calculando passagem')
print('=' * 52)
d = float(input('{}Qual será a distânçia de sua viagem em km? '.format('\033[33m')))
print('{}Você está prestes a começar uma viagem de {:.2f} km'.format('\033[36m', d))
p = d * 0.5 if d <= 200 else d * 0.45
print('E o preço a pagar será de R${:.2f}.'.format(p))
