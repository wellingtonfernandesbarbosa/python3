from time import sleep
al = float(input('{}Qual é a altura da parede: '.format('\033[34m')))
la = float(input('Qual é a largura da perede: {}'.format('\033[m')))
ar = al*la
li = ar/2
print('\033[33mCalculando...\033[m')
sleep(2)
print('{}Sua parede tem a dimensão de {}x{} e sua área é de {:.2f}m².'.format('\033[35m', al, la, ar))
print('Para pintar essa parede você precisará de {:.3f}l de tinta.{}'.format(li, '\033[m'))
