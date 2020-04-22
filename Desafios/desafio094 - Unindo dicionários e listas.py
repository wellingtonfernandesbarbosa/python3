from names import get_first_name
from random import randint

cadastro = dict()
pesssoas = list()
tanos = 0
r = sexo = ''

while True:
    cadastro['Nome'] = get_first_name()  # str(input('Nome: ')).capitalize()
    print(f'Nome: {cadastro["Nome"]}')
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'MF':  # Validação de dados tipo 1
        print('ERRO! Por favor, digite apenas M ou F.')
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    cadastro['Sexo'] = sexo
    cadastro['Idade'] = randint(5, 70)  # int(input('Idade: '))
    print(f'Idade: {cadastro["Idade"]}')
    tanos += cadastro['Idade']
    pesssoas.append(cadastro.copy())
    while True:  # Validação de dados tipo 2
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if r in 'SN':
            break
        print('ERRO! Por favor digite apenas S ou N.')
    if r == 'N':
        break

print('=' * 42)
print(f'- O grupo tem {len(pesssoas)} pessoas.')
print(f'- A média de idade é de {tanos / len(pesssoas)}.')
print('- As mulheres cadastradas são: ', end='')
for c in range(0, len(pesssoas)):
    if pesssoas[c]['Sexo'] == 'F':
        print(pesssoas[c]['Nome'], end=' ')
print()
print('- As pessoas com idade acima da média são:')
for c in range(0, len(pesssoas)):
    if pesssoas[c]['Idade'] > (tanos / len(pesssoas)):
        print(f'Nome = {pesssoas[c]["Nome"]}; Sexo = {pesssoas[c]["Sexo"]}; Idade = {pesssoas[c]["Idade"]}')
print('<< ENCERRADO >>')
