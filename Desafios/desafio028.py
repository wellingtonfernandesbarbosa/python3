from random import randint
print('Tente acertar o número de 0 a 5')
n = int(input('Digite um número de 0 a 5: '))
r = randint(0, 5)
if n == r:
    print('Parabéns, você acertou!')
    print('Vocês dois escolheram {}.'.format(n))
else:
    print('O computador venceu!.')
