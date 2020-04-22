print('=' * 37)
print('{:^37}'.format('BANCO DA PRAÇA'))
print('=' * 37)
v = int(input('Qual valor você quer sacar? '))
ced = 50
tced = 0
while True:
    if v >= ced:  # Teste para notas de R$ 50,00, mais a frente a nota é testada e volta a esse loop.
        v -= ced
        tced += 1
    else:
        if tced == 1:  # Strings no singular ou plural para a apresentação do resultado.
            print(f'Total de {tced} cédula de {ced}')
        elif tced > 1:
            print(f'Total de {tced} cédulas de {ced}')
        if ced == 50:  # Teste de notas possíveis.
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        tced = 0
        if v == 0:
            break
print('=' * 37)
print('Volte sempre ao BANCO DA PRAÇA!')
print('Tenha um bom dia.')
