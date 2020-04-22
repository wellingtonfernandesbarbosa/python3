menor = 0
maior = 0
for p in range(1, 5 + 1):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        menor = peso
        maior = peso
    if menor > peso:
        menor = peso
    elif maior < peso:
        maior = peso
print('O menor peso lido foi: {}Kg'.format(menor))
print('O maior peso lido foi: {}Kg'.format(maior))
