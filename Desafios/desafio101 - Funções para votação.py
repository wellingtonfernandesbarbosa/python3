from datetime import date


def voto(x):
    idade = date.today().year - x
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade <= 17 or idade > 65:
        return f'Com{idade} anos: VOTO OPICIONAL'
    elif 18 <= idade <= 64:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


print('=' * 30)
i = int(input('Em que ano você nasceu? '))
print(voto(i))
print('=' * 30)
