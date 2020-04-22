def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        num = input(msg)
        if num.isnumeric():
            ok = True
            valor = int(num)
        else:
            print(f'\033[0;31mErro! Digite um número inteiro válido\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}.')
