from datetime import date
print('{}='.format('\033[34m') * 60)
print(' ' * 23, 'Ano Bissexto')
print('=' * 60)
a = int(input('{}Que ano você quer analisar? Digite 0 para o ano atual: '.format('\033[33m')))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('{}O ano {} é BISSEXTO.'.format('\033[36m', a))
else:
    print('O ano {} NÃO é BISSEXTO.'.format(a))
