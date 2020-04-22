aluno = dict()
aluno['Nome'] = str(input('Nome: ')).capitalize()
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] < 5:
	aluno['Situação'] = 'Reprovado'
elif 5 <= aluno['Média'] < 7:
	aluno['Situação'] = 'Recuperação'
else:
	aluno['Situação'] = 'Aprovado'
print('=' * 33)
for k, v in aluno.items():
	print(f'  - {k} é igual a {v}')
