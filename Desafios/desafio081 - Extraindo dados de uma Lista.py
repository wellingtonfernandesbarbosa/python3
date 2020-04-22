lista = list()
c = 0
while True:
    novo = int(input('Digite um valor: '))
    lista.append(novo)
    c += 1
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
print('=' * 52)
print(f'Você digitou {c} elementos.')
lista.sort(reverse=True)
print('Os valores em ordem decrescente são:', lista)
if 5 in lista:
    print('O 5 faz parte da lista.')
else:
    print('O 5 não faz parte da lista.')
