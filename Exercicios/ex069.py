print('=' * 43)
print('{:^43}'.format('CADASTRE UMA PESSOA'))
print('=' * 43)
t = th = tm = 0
while True:
    i = int(input('Idade: '))
    s = r = ' '
    while s not in 'MF':
        s = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if i >= 18:
        t += 1
    if s == 'M':
        th += 1
    if s == 'F' and i < 20:
        tm += 1
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
if t == 1:
    print(f'Ao todo temos {t} pessoa com 18 anos ou mais.')
elif t > 1:
    print(f'Ao todo temos {t} pessoas com 18 anos ou mais.')
if th == 1:
    print(f'Ao todo temos {th} homem cadastrado.')
elif th > 1:
    print(f'Ao todo temos {th} homens cadastrados.')
if tm == 1:
    print(f'Ao todo temos {tm} mulher com menos de 20 anos.')
elif tm > 1:
    print(f'Ao todo temos {tm} mulher com menos de 20 anos.')
