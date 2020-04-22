from math import trunc

print('=' * 37)
print('{:^37}'.format('BANCO WJ'))
print('=' * 37)
valor = int(input('Qual valor você quer sacar? R$ '))
if valor >= 50:
    n50 = trunc(valor / 50)
    valor = valor % 50
    print(f'Total de {n50} cédulas de R$50')
if valor >= 20:
    n20 = trunc(valor / 20)
    valor = valor % 20
    print(f'Total de {n20} cédulas de R$20')
if valor >= 10:
    n10 = trunc(valor / 10)
    valor = valor % 10
    print(f'Total de {n10} cédulas de R$10')
if valor >= 1:
    n1 = trunc(valor / 1)
    print(f'Total de {n1} cédulas de R$1')
