def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mErro! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\nO usuário preferiu não digitar esse número.')
            return 0
            break
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            x = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mPor faveor, digite um número real válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\nO usuário preferiu não digitar esse número.')
            return 0
            break
        else:
            return x


i = leiaInt('Digite um número Inteiro: ')
f = leiaFloat('Digite um número Real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {f}.')
