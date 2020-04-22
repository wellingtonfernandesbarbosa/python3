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


def leiaDinheiro(x):
    valido = False
    while not valido:
        entrada = str(input('Digite um valor: ')).strip().replace(',', '.')
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mVocê digitou {entrada} que não é um dado válido!\33[m')
        else:
            valido = True
            return float(entrada)
