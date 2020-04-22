def leiaDinheiro(n):
    valido = False
    while not valido:
        entrada = str(input(n)).strip().replace(',', '.')
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mVocê digitou {entrada} que não é um dado valido!\033[m')
        else:
            valido = True
            return float(entrada)


def leiaInt(x):
    while True:
        if x.isnumeric():
            break
        else:
            print(f'\033[31mErro! Digite um número inteiro válido.\033[m')
            x = input('Digite um número: ')
    return x
