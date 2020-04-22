import pygame
m = input('{}Select the music: \nYesterday - Beatles[1] or Carry On My Wayward Son - Kansas[2] '.format('\033[34m'))
if m == 1:
    pygame.init()
    pygame.mixer.music.load('ex021.mp3')
    pygame.mixer.music.play()
    print('{}Playing Yesterday from Beatles...'.format('\033[34m'))
    pygame.event.wait()
if m == 2:
    pygame.init()
    pygame.mixer.music.load('ex021a.mp3')
    pygame.mixer.music.play()
    print('{}Carry On My Wayward Son - Kansas...'.format('\033[34m'))
    pygame.event.wait()

