"""Quando se tem um valor limite pode-se usar tanto while quanto range,
mas quando não se tem esse limite fica impossível utilizar o range"""
s = 0
'''for c in range(1, 8):
    n = int(input('Digite um valor: '))
    s += n
print('A soma dos valores é {}.'.format(s))'''
c = 1
while c < 8:
    n = int(input('Digite um valor: '))
    s += n
    c += 1
print('A soma dos valores é {}.'.format(s))
