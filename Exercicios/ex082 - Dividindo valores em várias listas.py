numeros = list()
par = list()
impar = list()
c = 0
while True:
    numeros.append(int(input('Digite um número: ')))
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if numeros[c] % 2 == 0:
        par.append(numeros[c])
    else:
        impar.append(numeros[c])
    c += 1
    if r in 'N':
        break
print('=' * 30)
print('A lista completa é:', numeros)
print('A lista de pares é:', par)
print('A lista de impares é:', impar)
