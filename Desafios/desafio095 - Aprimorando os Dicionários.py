from names import get_first_name
from random import randint

time = list()
jogador = dict()
gols = list()

while True:
    jogador.clear()
    gols.clear()
    jogador['Nome'] = get_first_name()  # str(input('Nome do(a) jogador(a): '))
    print(f'Nome do(a) jogador(a): {jogador["Nome"]}')
    partidas = randint(1, 5)  # int(input(f'Quantas partidas {jogador["Nome"]} jogou?'))
    print(f'Quantas partidas {jogador["Nome"]} jogou? {partidas}')
    for c in range(0, partidas):
        gol = randint(0, 4)
        print(f'   Quantos gols na partida {c}? {gol}')
        gols.append(gol)  # int(input(f'Quantos gols na partida {c + 1}? ')))
    jogador['Gols'] = gols[:]
    jogador['Total'] = total = sum(gols)
    time.append(jogador.copy())
    print(jogador)
    while True:
        r = str(input('Deseja cnontinuar? [S/N] ')).strip().upper()[0]
        if r in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if 'N' in r:
        break
    print('=' * 56)
print('=' * 56)

print('Cod  ', end='')
for i in jogador.keys():
    print(f'{i:<20}', end='')
print()
print('-' * 56)
for k, v in enumerate(time):
    print(f'{k + 1:>3}  ', end='')
    for d in v.values():
        print(f'{str(d):<20}', end='')
    print()
print('=' * 56)

while True:
    j = int(input('Deseja ver informações de qual jogador: (999 para parar) '))
    if j == 999:
        break
    while j < 1 or j > len(time) and j != 999:
        print(f'Não existe jogador com o código {j}!')
        print('-' * 56)
        j = int(input('Deseja ver informações de qual jogador: (999 para parar) '))
    if j == 999:
        break
    print(f' -- Levantamento do jogador(a) {time[j - 1]["Nome"]}:')
    for i, c in enumerate(time[j - 1]['Gols']):
        print(f'    Na {i + 1}ª partida fez {c} gols.')
    print('-' * 56)
print('<< VOLTE SEMPRE! >>')
