def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


def ParOuImpar(t):
    if t % 2 == 0:
        return True
    else:
        return False


print('Fatorial')
n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}!.')
print()
print('Par ou impar')
n = int(input('Digite um número: '))
if ParOuImpar(n):
    print(f'O número {n} é par.')
else:
    print(f'O número {n} é impar.')
