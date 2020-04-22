def multiplicação(x, y):
	return (x * y)
	

print('=' * 48)
print(f'{"Controle de terrenos":^48}')
print('-' * 48)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
print(f'A área de um terreno de {l}m x {c}m é de {multiplicação(l, c)}m².')
print('=' * 48)
