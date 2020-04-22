def linha(x):
	print('=' * x)
	
	
linha(32)
print(f'{"Decimal para binários":^32}')
linha(32)
while True:
	c = 128
	n = int(input('Digite um númerode 1 a 255: '))
	while n < 1 or n > 256:
		n = int(input('Número inválido! \nDigite um númerode 1 a 255:'))
	if n == 256:
		break
	for r in range(0, 8):
		if n >= c:
			print('1', end=' ')
			n = n - c
		else:
			print('0', end=' ')
		c = c / 2
	print()
	linha(32)
