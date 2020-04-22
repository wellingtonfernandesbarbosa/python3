pessoas = []
dados = []
menor = maior = 0
while True:
    dados.append(str(input('Nome: ')).capitalize())
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        menor = maior = dados[1]
    else:
        if dados[1] < menor:
            menor = dados[1]
        if dados[1] > maior:
            maior = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
print('=' * 52)
print(f'Ao todo foram cadastrados {len(pessoas)} pessoas.')
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
