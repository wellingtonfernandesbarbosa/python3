while True:
    n = int(input('Quer ver a tabuada de qual valor: '))
    print('-' * 38)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{c} x {n:2} = {c * n}')
    print('-' * 38)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
