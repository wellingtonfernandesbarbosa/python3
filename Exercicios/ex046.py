from time import sleep
print('=' * 21)
print(' Contagem regressiva')
print('=' * 21)
for c in range(10, -1, -1):
    print('{:2}'.format(c))
    sleep(1)
print('BOOM! BOOM! POOOW!')
