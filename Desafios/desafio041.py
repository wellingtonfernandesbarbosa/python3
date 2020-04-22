from datetime import date
a = int(input('Digite o ano de nascimento do atela: '))
i = date.today().year - a
if i <= 9:
    print('MIRIM')
elif i <= 14:
    print('INFANTIL')
elif i <= 19:
    print('JUNIOR')
elif i <= 20:
    print('SÉNIOR')
else:
    print('MASTER')
