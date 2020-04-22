numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'desesseis', 'desessete', 'desoito', 'desenove', 'vinte')
r = ''
while 'N' not in r:
    n = int(input('Digite um número entre 0 e 20: '))
    while 0 > n or n > 20:
        n = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {numeros[n]}.')
    r = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
print('Programa finalizado!')
