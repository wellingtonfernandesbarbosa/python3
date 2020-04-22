from datetime import date
print('{}='.format('\033[34m') * 28)
print(' ' * 3, 'Classificando Atletas')
print('=' * 28)
n = int(input('{}Ano de Nascimento: '.format('\033[33m')))
i = date.today().year - n
print('{}O atleta tem {} anos.'.format('\033[36m', i))
if i <= 9:
    print('Classificação: MIRIM')
elif i <= 14:
    print('Classificação: INFANTIL')
elif i <= 19:
    print('Classificação: JUNIOR')
elif i <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
