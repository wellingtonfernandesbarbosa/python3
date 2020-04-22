print('=' * 40)
print('{:^40}'.format('CADASTRE UMA PESSOA'))
print('=' * 40)
sexo = ' '
t = th = tm = 0
while True:
    i = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
    if i >= 18:
        t += 1
    if sexo in 'M':
        th += 1
    if sexo in 'F' and i <= 20:
        tm += 1
    print('-' * 40)
    q = str(input('Você quer continuar? [S/N] ')).strip().upper()
    print('-' * 40)
    if q == 'N':
        break
    sexo = ' '
print('{:=^40}'.format(' FIM DO PROGRAMA '))
print(f'Total de pessoas com mais de 18 anos: {t}')
print(f'Ao todo temos {th} homens cadastrados.')
print(f'E temos {tm} mulheres com menos de 20 anos.')
