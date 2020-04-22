from datetime import date
n = int(input('Em que ano você nasceu? '))
i = date.today().year - n
f = 18 - i
p = i - 18
if i < 18:
    print('Você ainda vai se alistar ao seviço militar. Falta {} anos.'.format(f))
elif i == 18:
    print('É hora de se alistar ao serviço militar.')
else:
    print('Já passou da idade de se alistar ao serviço militar. Já passou {} anos da idade de alistamento.'.format(p))
