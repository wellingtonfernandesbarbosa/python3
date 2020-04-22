times = ('Palmeiras', 'Santos', 'São Paulo', 'Atlético-MG', 'Botafogo', 'Athlético-PR',
         'Flamengo', 'Bahia', 'Goiás', 'Internacional', 'Cruzeiro', 'Corinthians',
         'Chapecoense', 'Ceará', 'Fluminense', 'Fortaleza', 'CSA', 'Grêmio', 'Avaí', 'Vasco')
print('=' * 63)
print(f'Os 5 primeiros colocados são: \n{times[:5]}')
print('=' * 63)
print(f'Os 4 últimos colocados são: \n{times[-4:]}')
print('=' * 63)
print(f'Veja o nome dos times em ordem alfabética: \n{sorted(times)}')
print('=' * 63)
print(f'O time da Chapecoense está na {times.index("Chapecoense") + 1}ª posição.')
