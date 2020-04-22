from datetime import datetime
cadastro = dict()
cadastro['Nome'] = str(input('Nome: ')).capitalize()
nasc = int(input('Ano de nascimento: '))
cadastro['Idade'] = datetime.now().year - nasc
cadastro['CTPS'] = int(input('Carteira de Trabalho(0 não tem): '))
if cadastro['CTPS'] != 0:
    cadastro['Contratação'] = int(input('Ano de Contratação: '))
    cadastro['Salário'] = float(input('Salário: '))
    cadastro['Aposentadoria'] = ((cadastro['Contratação'] + 35) - datetime.now().year) + cadastro['Idade']
print('=' * 45)
for k, v in cadastro.items():
    print(f'  - {k} tem o valor {v}')
