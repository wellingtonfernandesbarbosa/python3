from names import get_first_name
from random import randint
from time import sleep

jogador = dict()
gols = list()
lista = list()

while True:
    jogador['Nome'] = get_first_name()  # str(input('Nome do Jogador(a): '))
    print(f'Nome do jogador:', jogador['Nome'])
    partidas = randint(1, 5)  # int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    print(f'Quantas partidas {jogador["Nome"]} jogou? ', partidas)
    for c in range(0, partidas):
        sleep(0.5)
        gols.append(randint(0, 4))
        print(f'    Quantos gols na {c + 1}ª partida? {gols[c]}')
    jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols)
    lista.append(jogador.copy())
    gols.clear()
    print('=' * 60)
    while True:
        r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if r not in 'SN':
            print('ERRO! Responda apenas com S ou N.')
        if r in 'SN':
            break
    if r in 'N':
        break
print('=' * 60)
print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:<20}', end='')
print()
print('-' * 60)
for k, v in enumerate(lista):
    print(f'{k+1:^3} ', end='')
    for d in v.values():
        print(f'{str(d):<20}', end='')
    print()
print('=' * 60)
while True:
    j = int(input('Deseja ver informações de qual jogador? (999 para parar) '))
    if j == 999:
        break
    while j < 1 or j > len(lista) and j != 999:
        print(f'Não existe jogador com o código {j}!')
        print('-' * 60)
        j = int(input('Deseja ver informações de qual jogador? (999 para parar) '))
        if j == 999:
            break
    if j == 999:
        break
    print(f' -- Levantamento jogadora(a) {lista[j-1]["Nome"]}')
    for i, c in enumerate(lista[j-1]['Gols']):
        sleep(0.5)
        if c == 0:
            print(f'        Na {i + 1}ª partida não fez nenhum gol.')
        elif c == 1:
            print(f'        Na {i + 1}ª partida fez {c} gol.')
        else:
            print(f'        Na {i + 1}ª partida fez {c} gols.')
    print('=' * 60)
print('FINALIZANDO PROGRAMA...')
sleep(0.5)
print('<<< Programa finalizado, volte sempre! >>>')
