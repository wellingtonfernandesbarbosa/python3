print('Análise de notas')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terçeira nota: '))
n4 = float(input('Digite a quarta nota: '))
m = (n1+n2+n3+n4) / 4
print('Sua média de sua nota é {:.1f}'.format(m))
if m >= 6.0:
    print('{}Voçe atingiu a média.{}'.format('\033[32m', '\033[m'))
else:
    print('{}Sua nota está abaixo da média.{}'.format('\033[31m', '\033[m'))

print('\033[34mPARABÉNS!\033[m' if m >= 6.0 else '\033[31mESTUDE MAIS!\033[m')
