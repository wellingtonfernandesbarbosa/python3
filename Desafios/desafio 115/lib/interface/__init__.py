def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar o número.\033[m')
            return 3
            break
        else:
            return n


def cabeçalho(msg):
    linha()
    print(msg.center(42))
    linha()


def menu(lista):
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    opc = leiaInt('\033[32mDigite sua opção: \033[m')
    return opc


def linha(tam=42):
    print('=' * tam)
