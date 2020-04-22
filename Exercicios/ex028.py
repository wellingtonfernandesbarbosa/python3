from random import randint
from time import sleep
jn = 'S'
player = 0
pc = 0
while jn == 'S':
    print('{}-=-'.format('\033[36m') * 19)
    print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
    print('-=-' * 19)
    n = int(input('{}Em que número você pensou? '.format('\033[33m')))
    r = randint(0, 5)
    print('{}PROCESSANDO...'.format('\033[31m'))
    sleep(0.7)
    if n == r:
        print('{}PARABÉNS! Você conseguiu me vencer!'.format('\033[34m'))
        player = player + 1
    else:
        print('{}GANHEI! Eu pensei no número {} e não no número {}.'.format('\033[31m', r, n))
        pc = pc +1
    jn = input('{}Vamos jogar de novo? [S/N] '.format('\033[33m')).upper()
print('{}Você marcou {} ponto(s).'.format('\033[34m', player))
print('Eu marquei {} ponto(s).'.format(pc))
