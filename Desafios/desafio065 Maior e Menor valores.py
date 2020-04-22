r = 'S'
menor = maior = c = s = 0
while r == 'S':
    n = int(input('Digite um número: '))
    s += n
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if menor > n:
            menor = n
        if maior < n:
            maior = n
    r = str(input('Você quer continuar [S/N]? ')).upper()[0]
media = s / c
print('A média dos {} valores é {:.2f}.'.format(c, media))
print('O menor é {} e o maior valor é {}.'.format(menor, maior))
