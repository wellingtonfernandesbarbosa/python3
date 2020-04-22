from time import sleep
n1 = int(input('Início: '))
n2 = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(n1, n2+1, p):
    print(c)
    sleep(0.1)
print('Fim')