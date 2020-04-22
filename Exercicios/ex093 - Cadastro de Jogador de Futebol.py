from names import get_first_name
from random import randint

jogador = dict()
gols = list()

jogador['Nome'] = get_first_name()  # str(input('Nome do(a) jogador(a): '))
print(f'Nome do(a) jogador(a): {jogador["Nome"]}')
partidas = randint(1, 5)  # int(input(f'Quantas partidas {jogador["Nome"]} jogou?'))
print(f'Quantas partidas {jogador["Nome"]} jogou? {partidas}')
for c in range(0, partidas):
    gols.append(randint(0, 4))  # int(input(f'Quantos gols na partida {c + 1}? ')))
jogador['Gols'] = gols
jogador['Total'] = total = sum(gols)
print('=' * 56)
print(jogador)

print('=' * 56)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('=' * 56)
if len(jogador['Gols']) == 1:
    print(f'O jogador(a) {jogador["Nome"]} jogou {len(jogador["Gols"])} partida.')
else:
    print(f'O jogador(a) {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas.')
for i, c in enumerate(jogador['Gols']):
    if c == 0:
        print(f'  - Na partida {i + 1} não fez nenhum gol.')
    elif c == 1:
        print(f'  - Na partida {i + 1} fez {c} gol.')
    else:
        print(f'  - Na partida {i + 1} fez {c} gols.')
print('=' * 56)
