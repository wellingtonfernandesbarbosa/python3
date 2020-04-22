from random import randint
sorteio = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram: {sorteio}')
menor = ' '
maior = 0
for c in range(0, 5):
    if menor == ' ':
        menor = sorteio[c]
    if menor > sorteio[c]:
        menor = sorteio[c]
    if maior < sorteio[c]:
        maior = sorteio[c]
print(f'O menor número é {menor}.')
print(f'O maior número é {maior}.')
