c = s = stop = 0
while stop != 999:
    n = int(input('Digite um número [999 para parar]: '))
    stop = n
    c += 1
    if n != 999:
        s += n
print('Você digitou {} números e a soma deles é {}.'.format(c, s))
