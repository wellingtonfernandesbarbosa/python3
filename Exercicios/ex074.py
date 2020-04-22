from random import randint
n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram: ', end='')
for t in n:
    print(t, end=' ')
print(f'\nO menor valor foi : {min(n)}')
print(f'E o maior valor sorteado foi: {max(n)}')
