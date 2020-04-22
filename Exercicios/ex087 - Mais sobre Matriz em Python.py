matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sp = stc = mvsc = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {l}]: '))
        if matriz[l][c] % 2 == 0:
            sp += matriz[l][c]
        if matriz[1][c] > mvsc:
            mvsc = matriz[1][c]
    if matriz[l][2]:
        stc += matriz[l][2]
print('=' * 32)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print('=' * 32)
print(f'A soma dos valores pares é {sp}.')
print(f'A soma dos valores da terceira coluna é {stc}.')
print(f'O maior valor da segunda coluna é {mvsc}.')
