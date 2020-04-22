numeros = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais número: ')),
           int(input('Digite o último número: ')))
print('=' * 34)
print(f'Você digitou os números: ', end='')
for t in numeros:
    print(t, end=' ')
if numeros.count(9) == 1:
    print(f'\nO número 9 apareceu {numeros.count(9)} vez.')
elif numeros.count(9) > 1:
    print(f'\nO número 9 apareceu {numeros.count(9)} vezes.')
else:
    print('\nO número 9 não foi digitado.')
if 3 in numeros:
    print(f'O número 3 apareceu na {numeros.index(3) + 1}ª posição.')
else:
    print('O valor 3 não foi digitado.')
print(f'Os números pares são: ', end='')
for t in numeros:
    if t % 2 == 0:
        print(t, end=' ')
print('.')
print('=' * 34)
