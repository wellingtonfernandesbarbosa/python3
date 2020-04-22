n = float(input('{}Quantos reais você tem? R$ {}'.format('\033[1;32m', '\033[m')))
print('{}Com R${:.2f} você pode comprar US$ {:.2f}.'.format('\033[34m', n, (n/3.86)))
print('Com R${:.2f} você pode comprar € {:.2f}.{}'.format(n, (n/4.40), '\033[m'))
