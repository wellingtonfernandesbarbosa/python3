pessoas = list()
dados = list()
c = menor = maior = 0
while True:
    dados.append(str(input('Nome: ')))
    peso = float(input('Peso: '))
    dados.append(peso)
    pessoas.append(dados[:])
    dados.clear()
    r = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
    if menor == 0 or maior == 0:
        menor = peso
        maior = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso
    if r in 'N':
        break
print('=' * 50)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for c in pessoas:
    if c[1] == menor:
        print(c[0], end=' ')
print(f'\nO menor peso foi de {maior}Kg. Peso de ', end='')
for c in pessoas:
    if c[1] == maior:
        print(c[0], end=' ')
print()
