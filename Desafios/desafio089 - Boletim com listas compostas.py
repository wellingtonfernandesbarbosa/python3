import names
from random import randint
lista = []
notas = []
alunos = []
while True:
    nome = names.get_first_name()
    nota1 = randint(4, 10)
    nota2 = randint(5, 10)
    media = (nota1 + nota2) / 2
    notas.append(nota1)
    notas.append(nota2)
    alunos.append(nome)
    alunos.append(notas[:])
    alunos.append(media)
    lista.append(alunos[:])
    print(alunos)
    notas.clear()
    alunos.clear()
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
print('=' * 22)
print(f'{"Nº  NOME":<15} MÉDIA')
for c in range(0, len(lista)):
    print('{:<3} {:<12} {}'.format((c + 1), (lista[c][0]), lista[c][2]))
while True:
    print('-' * 50)
    mostrar = int(input('Mostrar notas para qual aluno? {999 interrompe): '))
    if mostrar == 999:
        break
    if 0 > mostrar or mostrar > len(lista):
        mostrar = int(input('Mostrar notas para qual aluno? {999 interrompe): '))
    print(f'As notas de {lista[mostrar - 1][0]} são {lista[mostrar - 1][1]}')
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
