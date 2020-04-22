from time import sleep
n = int(input('Digite o primeiro termo: '))
r = int(input('Qual é a razão: '))
for c in range(0, 10):
    print(n)
    n = n + r
    sleep(0.1)
