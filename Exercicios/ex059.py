from time import sleep
o = 0
while o != 5 or o == 4:
    n1 = int(input('Primeiro valor: '))
    n2 = int(input('Segundo valor: '))
    while o != 5:
        print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
        o = int(input('>>> Qual é a sua opção? '))
        if o == 1:
            print('A soma ente {} e {} é {}.'.format(n1, n2, n1 + n2))
        elif o == 2:
            print('{} multiplicado por {} é {}.'.format(n1, n2, n1 * n2))
        elif o == 3:
            if n1 > n2:
                maior = n1
            elif n1 < n2:
                maior = n2
            else:
                print('Os dois valores são iguais.')
            print('Entre {} e {} o maior valor é {}.'.format(n1, n2, n2))
        if o == 4:
            print('Informe os valores novamente: ')
            n1 = int(input('Primeiro valor: '))
            n2 = int(input('Segundo valor: '))
        if o == 5:
            print('Finalizando...')
        if o < 0 or o > 5:
            print('{}Opção inválida. tente novamente.{}'.format('\033[31m', '\033[m'))
        print('=-=' * 11)
sleep(1)
print('Programa finalizado com sucesso.')

