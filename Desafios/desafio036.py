print('=' * 36)
print(' ' * 5, 'Análise de financiamento')
print('=' * 36)
s = float(input('Qual o valor do seu salario? '))
c = float(input('Qual o valor da casa? '))
a = int(input('Em quantos anos pretende pagar? '))
m = a * 12
if c/m <= (30 * (s / 100)):
    print('Parabéns. Seu crédito foi aprovado.')
else:
    print('Infelismente seu crédito não foi apeovado.')
