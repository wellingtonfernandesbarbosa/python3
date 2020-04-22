print('{}='.format('\033[34m') * 48)
print(' ' * 11, 'Financiamento Imobiliário')
print('=' * 48)
c = float(input('{}Qual o valor da casa? R$ '.format('\033[33m')))
s = float(input('Qual o salário do comprador? R$ '))
a = int(input('Quantos anos de financiamento? '))
m = a * 12
p = c / m
su = s * 30 / 100
if p <= su:
    print('{}O financiamento foi aprovado.'.format('\033[32m'))
    print('Para financiar em {} meses a parcela será de R${:.2f}.'.format(m, p))
else:
    print('Para pagar uma casa de R${:.2f} o valor mínimo da parcela é de R${:.2f}.'.format(c, p))
    print('{}Financiamento negado!'.format('\033[31m'))
