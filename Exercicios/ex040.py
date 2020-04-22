print('{}='.format('\033[34m') * 21)
print(' ' * 3, 'Média de aluno')
print('=' * 21)
n1 = float(input('{}Primeira nota: '.format('\033[33m')))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('{}Com média de {:.1f} o aluno está REPROVADO.'.format('\033[31m', m))
elif 5 <= m < 7:
    print('{}Com média de {:.1f} o aluno está de RECUPERAÇÂO.'.format('\033[33m', m))
elif m >= 7:
    print('{}Com média de {:.1f} o aluno está APROVADO.'.format('\033[36m', m))
