n1 = int(input(f'Digite o 1º Valor: '))
n2 = int(input(f'Digite o 2º Valor: '))
n3 = int(input(f'Digite o 3º Valor: '))
n4 = int(input(f'Digite o 4º Valor: '))
numeros = (n1, n2, n3, n4)
print(f'Você digitou os valores: ', end='')
for t in numeros:
    print(t, end=' ')
print(f'\nO número 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O número 3 foi encontrado na {numeros.index(3) + 1}ª posição.')
else:
    print('O valor 3 não foi encontrado em nenhuma posição')
print(f'Os números pares são: ', end='')
if numeros[0] % 2 == 0:
    print(f'{numeros[0]}', end='')
if numeros[1] % 2 == 0:
    print(f' {numeros[1]}', end='')
if numeros[2] % 2 == 0:
    print(f' {numeros[2]}', end='')
if numeros[3] % 2 == 0:
    print(f' {numeros[3]}', end='')
print('.')
