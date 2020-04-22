from names import get_first_name
from random import randint
jogador = dict()
gols = list()
s = 0

jogador['Nome'] = get_first_name()  # str(input('Nome do jogador: '))
print(f'Nome: {jogador["Nome"]}')
partidas = randint(0, 5)  # int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
print(f'Quantas partidas {jogador["Nome"]} jogou? {partidas}')
for c in range(0, partidas):
    gol = randint(0, 4)  # int(input(f'Quantos gols na partida {c + 1}? '))
    s += gol
    gols.append(gol)
jogador['Gols'] = gols
jogador['Total'] = s
print('=' * 56)

print(jogador)
print('=' * 56)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('=' * 56)
print(f'O jogador {jogador["Nome"]} jogou {partidas}.')
for c, v in enumerate(jogador['Gols']):
    print(f'    => Na partida {c + 1}, fez {v} gols.')
print(f'Foi um total de {jogador["Total"]} gols.')
