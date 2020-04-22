"""Quando se tem um valor limite pode-se usar tanto while quanto range,
mas quando não se tem esse limite fica impossível utilizar o range"""
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares.'.format(par, impar))
"""Nesse caso o 'n' serve como interrupção do processo caso seu valor seja '0'"""
