def multiplicar(x, y):
    return x * y


print('=' * 48)
print(f'{"Controle de Terrenos":^48}')
print('-' * 48)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
print(f'A área de um terreno {l} x {c} é de {multiplicar(l, c)}m²')
print('=' * 48)
