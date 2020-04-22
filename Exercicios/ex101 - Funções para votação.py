def voto(x):
    from datetime import datetime
    x = datetime.today().year - x
    print(f'Com {x} anos: ', end='')
    if x < 16:
        print('NÃO VOTA.')
    elif 16 <= x < 18 or x > 65:
        print('VOTO OPCIONAL.')
    else:
        print('VOTO OBRIGATÓRIO.')


print('=' * 30)
a = int(input('Em que ano você nasceu? '))
voto(a)
print('=' * 30)
