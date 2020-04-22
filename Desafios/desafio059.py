from time import sleep
o = 0
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
while o != 5:
    print('''[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa''')
    o = int(input('Qual sua opção: '))
    if o == 1:
        print(n1 + n2)
    elif o == 2:
        print(n1 * n2) 
    elif o == 3:
        if n1 > n2:
            print('{} é o maior.'.format(n1))
        elif n1 < n2:
            print('{} é o maior.'.format(n2))
    elif o == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif o == 5:
        print('Finalizando...')
        sleep(0.5)
        print('Programa finalizado com sucesso.')
    else:
        print('Opção inválida. Tente novamente')
    print('=' * 32)
