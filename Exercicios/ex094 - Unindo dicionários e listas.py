from names import get_first_name
from random import randint
cadastro = dict()
pessoas = list()
tanos = 0

while True:
    cadastro['Nome'] = get_first_name()
    print(f'Nome: {cadastro["Nome"]}')
    cadastro['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while cadastro['Sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        cadastro['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    cadastro['Idade'] = randint(13, 70)
    tanos += cadastro['Idade']
    print(f'Idade: {cadastro["Idade"]}')
    pessoas.append(cadastro.copy())
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while r not in 'SN':
        print('ERRO! Responda apenas com S ou N.')
        r = str(input('Quer continuar? [S/N] '))
    if r in 'N':
        break
print('=' * 42)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {tanos / len(pessoas)} anos.')
print('C) As mulheres cadastradas foram: ', end='')
for c in pessoas:
    if c['Sexo'] == 'F':
        print(c['Nome'], end=' ')
print()
print('D) Lista das pessoas que estão acima da média:')
for c in pessoas:
    if c['Idade'] > (tanos/len(pessoas)):
        print(f'Nome = {c["Nome"]}; Sexo = {c["Sexo"]}; Idade = {c["Idade"]}')
print('<<< ENCERRADO >>>')
