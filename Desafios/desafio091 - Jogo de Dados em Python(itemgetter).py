from random import randint
from time import sleep
from operator import itemgetter
jogadores = dict()
ranking = list()
jogadores['jogador1'] = randint(1, 6)
jogadores['jogador2'] = randint(1, 6)
jogadores['jogador3'] = randint(1, 6)
jogadores['jogador4'] = randint(1, 6)
print('Valores sorteados: ')
for i, v in jogadores.items():
	print(f'O {i} tirou {v}.')
	sleep(0.3)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)  # Função EXTREMAMENTE IMPORTATE
for i, v in enumerate(ranking):
	print(f'{i+1}º lugar: {v[0]} tirou {v[1]}.')
	sleep(0.3)
