from random import randint
jogador = 1
computador = t = 0
print('Vou pensar em um número de 0 a 10, tente acertar!')
while computador != jogador:
    computador = randint(0, 10)
    jogador = int(input('O número que vocẽ pensou foi: '))
    if computador != jogador:
        print('Não!')
    t += 1
print('Parabéns, você acertou. mas vocẽ precisou de {} tentativas.'.format(t))
