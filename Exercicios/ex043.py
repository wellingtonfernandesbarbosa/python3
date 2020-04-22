print('{}-=-'.format('\033[36m') * 9)
print(' ' * 5, 'Cálculo de IMC')
print('-=-' * 9)
p = float(input('{}Qual é seu peso? (Kg) '.format('\033[33m')))
a = float(input('Qual é sua altura? (m) '))
imc = p / a**2
print('{}Seu IMC é {:.1f}'.format('\033[34m', imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal.')
elif imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL.')
elif imc < 30:
    print('{}Você está em SOBREPESO!'.format('\033[33m'))
elif imc < 40:
    print('{}Você está em OBESIDADE!'.format('\033[31m'))
elif imc >= 40:
    print('{}Você está em OBESIDADE MÓRBIDA, Cuidado!'.format('\033[31m'))
