numeros = list()
while True:
    numeros.append(int(input('Digite um valor: ')))
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
print('=' * (40 + (len(numeros) * 2)))
if len(numeros) == 1:
    print(f'Você digitou {len(numeros)} elemento.')
else:
    print(f'Você digitou {len(numeros)} elementos.')
numeros.sort(reverse=True)
print('Os valores em ordem decescente são:', numeros)
if 5 in numeros:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')
