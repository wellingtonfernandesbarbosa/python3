from time import sleep


def contador(x, y, z):
	print(f'Contagem de {x} a {y} de {z} em {z}')
	if x > y:
		z = z * -1
		for t in range(x, y - 1, z):
			print(t, end=' ', flush=True)
			sleep(0.4)
		print('FIM!')
	elif y > x:
		for t in range(x, y + 1, z):
			print(t, end=' ', flush=True)
			sleep(0.4)
		print('FIM!')


print('=' * 30)
print('Contagem de 1 até 10 de 1 em 1')
for c in range(1, 11):
	print(c, end=' ', flush=True)
	sleep(0.4)
print('FIM!')
print('=' * 30)
print('Contagem de 10 até 1 de 2 em 2')
for c in range(10, 0, -2):
	print(c, end=' ', flush=True)
	sleep(0.4)
print('FIM!')
print('=' * 30)
print('Agora é a sua vez de personalizar a a contagem!')
i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
if p < 0:
	p *= -1
elif p == 0:
	p = 1
contador(i, f, p)
