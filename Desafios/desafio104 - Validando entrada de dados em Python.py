def leiaInt(x):
    while True:
        if x.isnumeric():
            break
        else:
            print(f'\033[31mErro! Digite um número inteiro válido.\033[m')
            x = input('Digite um número: ')
    return x


n = leiaInt(input('Digite um número: '))
print(f'Você acabou de digitar o número {n}.')
