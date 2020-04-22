from time import sleep


def contador(x, y, z):
    if x < y:
        print(f'Contando de {x} até {y} de {z} em {z}')
        for t in range(x, y + 1, z):
            print(t, end=' ', flush=True)
            sleep(0.5)
        print('FIM!')
    if x > y:
        print(f'Contando de {x} até {y} de {z} em {z}')
        for t in range(x, y - 1, -z):
            print(t, end=' ', flush=True)
            sleep(0.5)
        print('FIM!')


print('=' * 44)
print('Contagem de 1 até 10 de 1 em 1')
for c in range(1, 11):
    print(c, end=' ', flush=True)
    sleep(0.5)
print()
print('=' * 44)
print('Contagem de 10 a 0 de 2 em 2')
for c in range(10, -1, -2):
    print(c, end=' ', flush=True)
    sleep(0.5)
print()
print('=' * 44)
print('Agora é a sua vez de personalizar a contagem')
i = int(input('Início:  '))
f = int(input('Fim:     '))
p = int(input('Passo:   '))
if p == 0:
    p = 1
if p < 0:
    p *= -1
contador(i, f, p)
print('=' * 44)
