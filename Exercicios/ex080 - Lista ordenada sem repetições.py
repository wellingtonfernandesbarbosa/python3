lista = list()
print('=' * 47)
print(f'\033[31m{"VALORES EM ORDEM S/ .sort()":^47}\33[m')
print('=' * 47)
for c in range(0, 5):
    novo = int(input('Digite um número: '))
    if c == 0 or novo > lista[-1]:
        lista.append(novo)
        print('Valor adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if pos <= lista[pos]:
                lista.insert(pos, novo)
                print(f'Valor adicionadao na posição {pos}...')
                break
            pos += 1
print('=' * 47)
print('Os valores digitados em ordem foram:', end='')
for c in range(0, 5):
    print(f' {lista[c]}', end='')
print('.')
print('=' * 47)
