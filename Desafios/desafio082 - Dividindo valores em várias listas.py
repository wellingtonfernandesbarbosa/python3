lista = list()
par = list()
impar = list()
c = 0
while True:
    novo = int(input('Digite um valor: '))
    lista.append(novo)
    if lista[c] % 2 == 0:
        par.append(novo)
    else:
        impar.append(novo)
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
    c += 1
print('=' * 38)
print(f'A lista completa é:', lista)
print(f'A lista de pares é:', par)
print(f'A lista de impares é:', impar)
