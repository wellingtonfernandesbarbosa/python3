import pygame
from time import sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
print('{}='.format('\033[34m') * 20)
print('Vamos jogar Jokenpô?')
print('=' * 20)
print('''Suas opções: 
[ 0 ] Pedra 
[ 1 ] Papel 
[ 2 ] Tesoura''')
jogador = int(input('Qual sua jogada? '))
computador = randint(0, 2)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
print('-=-' * 8)
print('''Computador jogou {}
Jogador jogou {}'''.format(itens[computador], itens[jogador]))
print('-' * 24)
if itens[computador] == itens[jogador]:
    print('EMPATE')
elif computador == 0:
    if jogador == 1:
        print('JOGADOR GANHOU!')
        pygame.init()
        pygame.mixer.music.load('ganhou.mp3')
        pygame.mixer.music.play()
        pygame.event.wait()
    elif jogador == 2:
        print('COMPUTADOR GANHOU!')
        pygame.init()
        pygame.mixer.music.load('perdeu.mp3')
        pygame.mixer.music.play()
        pygame.event.wait()
    else:
        print('Opção Inválida.')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR GANHOU!')
        pygame.init()
        pygame.mixer.music.load('perdeu.mp3')
        pygame.mixer.music.play()
        pygame.event.wait()
    elif jogador == 2:
        print('JOGADOR GANHOU!')
        pygame.init()
        pygame.mixer.music.load('ganhou.mp3')
        pygame.mixer.music.play()
        pygame.event.wait()
    else:
        print('Opção Inválida.')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR GANHOU!')
        pygame.init()
        pygame.mixer.music.load('ganhou.mp3')
        pygame.mixer.music.play()
        pygame.event.wait()
    elif jogador == 1:
        print('COMPUTADOR GANHOU!')
        pygame.init()
        pygame.mixer.music.load('perdeu.mp3')
        pygame.mixer.music.play()
        pygame.event.wait()
    else:
        print('Opção Inválida')
print('-=-' * 8)
