alunos = []
while True:
    nome = str(input('Nome: '))
    nota1 = int(input('Nota 1: '))
    nota2 = int(input('Nota 2: '))
    alunos.append([nome, [nota1, nota2], (nota1 + nota2) / 2])
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('=' * 26)
print(f'{"Nº":<4}{"Nome":<10}{"Média":>7}')
print('-' * 26)
for i, c in enumerate(alunos):
    print(f'{i + 1:<4}{c[0]:<10}{c[2]:>7.1f}')
print('=' * 26)
while True:
    p = int(input('Mostrar notas de qual aluno? (999 para parar) '))
    if p == 999:
        break
    if 1 <= p <= len(alunos):
        print(f'As notas de {alunos[p - 1][0]} são {alunos[p - 1][1]}')
    print('=' * 48)
print('PROGRAMA FINALIZADO.')
print('<< VOLTE SEMPRE! >>')
