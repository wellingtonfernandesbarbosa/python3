def jogador(nome='<desconhecido>', gol=0):
    print(f'O jogador {nome}, fez {gol} gol(s) no campeonato.')


print('=' * 42)
n = input('Nome do Jogador: ').capitalize()
g = input('Número de Gols: ')
if g.isnumeric():  # Verifica se o item informado pelo usuário é um número
    g = int(g)
else:
    g = 0
if n.strip() == '':  # Se o campo nome estiver vazio, é passado para a função apenas o valor de gols.
    jogador(gol=g)
else:
    jogador(nome=n, gol=g)
print('=' * 42)
