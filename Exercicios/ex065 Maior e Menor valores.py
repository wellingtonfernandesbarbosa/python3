r = 'S'
c = s = maior = menor = media = 0
while r in 'S':
    n = int(input('Digite um número: '))
    c += 1
    s += n
    if c == 1:
        menor = maior = n
    else:
        if menor > n:
            menor = n
        if maior < n:
            maior = n
    r = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
media = s / c
print('A média dos {} valores é {}.'.format(c, media))
print('O menor valor é {} e o maior é {}.'.format(menor, maior))
