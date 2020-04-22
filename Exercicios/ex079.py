numeros = list()
print('=' * 35)
print(f'\033[31m{"LISTA ÚNICA ORDENADA":^35}\033[m')
print('=' * 35)
while True:
    novo = int(input('Digite um número: '))
    if novo not in numeros:
        numeros.append(novo)
        print('Valor adicionadao com sucesso...')
    else:
        print('Valor duplicado, não vou adicionar...')
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
print('=' * 35)
numeros.sort()
print('Você adicionou os números:', end='')
for c in range(0, len(numeros)):
    print(f' {numeros[c]}', end='')
print('.')
print('=' * 35)
