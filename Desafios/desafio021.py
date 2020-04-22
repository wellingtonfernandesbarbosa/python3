import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
print('{}Playing Yesterday from Beatles...'.format('\033[34m'))
pygame.event.wait()
