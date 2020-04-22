from time import sleep
print('{}='.format('\033[36m') * 20)
print('      TABUADA')
print('=' * 20)
n = int(input('Digite um número: {}'.format('\033[m')))
print('{}='.format('\033[32m') * 20)
c = 1
while c <= 10:
    print('{} x {:2} = {}'.format(n, c, (n*c)))
    c = c + 1
    sleep(0.7)
print('=' * 20)
