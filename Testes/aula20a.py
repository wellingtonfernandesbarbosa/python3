def soma(a, b):
    print(f'A = {a} e B = {b}')
    print(f'A soma de A + B = {a + b}')


def soma1(*valores):
    s = 0
    for v in valores:
        s += v
    print(f'Somando os valores {valores} temos {s}.')


a = int(input('1º número: '))
b = int(input('2º número: '))
soma(a, b)
soma(b=7, a=5)

soma1(5, 2)
soma1(2, 9, 4)
