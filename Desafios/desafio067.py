c = 1
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('=' * 38)
    while c <= 10:
        print(f'{n}  x {c:2} = {n * c}')
        c += 1
    print('=' * 38)
    c = 1
print('PROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE!')
