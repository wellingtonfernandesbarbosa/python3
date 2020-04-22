menor = 0
maior = 0
for c in range(1, 5 + 1):
    p = float(input('Peso da {}ª pessoa: '.format(c)))
    if menor > p or menor == 0:
        menor = p
    if maior < p:
        maior = p
print('O menor peso lido foi: {}Kg'.format(menor))
print('O maior peso lido foi: {}Kg'.format(maior))
