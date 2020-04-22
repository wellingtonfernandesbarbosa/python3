from datetime import date
print('{}='.format('\033[34m') * 40)
print(' ' * 10, 'Alistamento Militar')
print('=' * 40)
n = int(input('{}Ano de nascimento: '.format('\033[33m')))
i = date.today().year - n
if i < 18:
    print('{}Quem nasceu em {} tem {} anos em {}.'.format('\033[35m', n, i, date.today().year))
    print('Seu alistamento será em {}.'.format(n + 18))
elif i == 18:
    print('{}Quem nasceu em {} tem {} anos em {}.'.format('\033[36m', n, i, date.today().year))
    print('Você tem que se alistar IMEDIATAMENTE!')
else:
    print('{}Quem nasceu em {} tem {} anos em {}.'.format('\033[35m', n, i, date.today().year))
    print('Você deveria ter se alistado há {} anos.'.format(date.today().year - (n + 18)))
    print('Seu alistamento foi em {}.'.format(n + 18))
