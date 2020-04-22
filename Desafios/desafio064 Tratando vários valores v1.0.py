c = s = stop = 0
while stop != 999:
    n = int(input('Digite um número: '))
    stop = n
    c += 1
    if n != 999:
        s += n
print('Você digitou {} números.'.format(c))
print('A soma dos números digitados é {}.'.format(s))
