lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
#  Tuplas são IMUTÁVEIS

print(sorted(lanche))  # Para colocar em ordem

for c in lanche:
    print(f'Eu vou comer {lanche}')

for c in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[c]} na posição {c}.')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}.')

print('Comi para caramba!')
