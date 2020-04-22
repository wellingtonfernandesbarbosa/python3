from datetime import date
from names import get_first_name
cadastro = dict()

cadastro['Nome'] = get_first_name()  # str(input('Nome: '))
print(f'Nome: {cadastro["Nome"]}')
nasc = int(input('Data de nascimento: '))
cadastro['Idade'] = date.today().year - nasc
cadastro['CTPS'] = int(input('Carteira de trabalho (0 não tem):'))

if cadastro['CTPS'] != 0:
	cadastro['Contratação'] = int(input('Ano de contratação: '))
	cadastro['Salário'] = float(input('Valor do Salário: R$'))
	cadastro['Aposentadoria'] = ((cadastro['Contratação'] + 35) - date.today().year) + cadastro['Idade']
print('=' * 45)

print(cadastro)
for k, v in cadastro.items():
	print(f'{k} tem o valor {v}')
