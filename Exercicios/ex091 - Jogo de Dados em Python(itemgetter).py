from random import randint
from time import sleep
from operator import itemgetter
from names import get_first_name
ranking = list()
jogo = {get_first_name(): randint(1, 6),
        get_first_name(): randint(1, 6),
        get_first_name(): randint(1, 6),
        get_first_name(): randint(1, 6)}
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)  # Função EXTREMAMENTE IMPORTATE
print('==== RANKING DOS JOGADORES ====')
for i, v in enumerate(ranking):
    print(f'    {i + 1}º lugar: {v[0]} tirou {v[1]}')
    sleep(0.5)
