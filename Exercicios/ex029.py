print('{}='.format('\033[36m') * 61)
print(' ' * 27, 'RADAR')
print('=' * 61)
v = float(input('{}Qual a velocidade atual do carro? '.format('\033[33m')))
if v <= 80:
    if v < 55:
        print('{}Você está muito abaixo da velocidade permitida. CUIDADO!'.format('\033[34m'))
else:
    print('{}MULTADO! Você excedeu o limite de velocidade que é de 80Km/h.'.format('\033[31m'))
    if v >= 150:
        print('{}Tá maluco? Quer morrer?{}'.format('\033[1;31m', '\033[m'))
    print('{}Você deve pagar uma multa de R${:.2f}!'.format('\033[31m', (v-80) * 7))
print('{}Tenha um bom dia, DIRIJA COM SEGURANÇA!'.format('\033[32m'))
