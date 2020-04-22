n = int(input('Digite o primeiro termo: '))
r = int(input('Qual a razão? '))
c = p = 0
while c <= 10 + p:
    print('{}'.format(n), end='')
    print(',' if c < 9 else '.', end=' ')
    n += r
    c += 1
    while c == 10 + p:
        s = int(input('\nSe quiser continuar digite mais quantos números você quer, se não quiser digite 0: '))
        p += s
        if s == 0:
            print('Foram mostrados {} termos da P.A.'.format(c))
            print('Acabou!')
            c += 1
        else:
            while c <= 10 + p - 1:
                print('{}'.format(n), end='')
                print(',' if c < 10 + p - 1 else '.', end=' ')
                n += r
                c += 1
