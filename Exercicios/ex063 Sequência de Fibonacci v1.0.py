print('=' * 45)
print('{: ^36}'.format('Sequência Fibonacci'))
print('=' * 45)
n = int(input('Deseja ver quantos números da sequência? '))
t1 = 0
t2 = 1
print('=' * 45)
print('{} -> {} -> '.format(t1, t2), end='')
c = 3
while c <= n:
    t3 = t1 + t2
    print('{} -> '.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1
print('FIM')
print('=' * 45)
