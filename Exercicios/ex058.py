from random import randint
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?')
c = randint(0, 10)
t = 0
acertou = False
while not acertou:
    j = int(input('Qual o seu palpite? '))
    t += 1
    if j == c:
        acertou = True
    else:
        if j < c:
            print('É mais que {}. Tente mais uma vez.'.format(j))
        elif j > c:
            print('É menos que {}. Tente mais uma vez.'.format(j))
print('Você acertou com {} tentativas. Parabéns!'.format(t))

