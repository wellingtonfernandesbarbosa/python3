lista = list()
while True:
    novo = (int(input('Digite um valor: ')))
    if novo not in lista:
        lista.append(novo)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    pergunta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if pergunta == 'N':
        break
lista.sort()
print('=' * 37)
print(f'Você digitou os valores:', end=' ')
for c in range(0, len(lista)):
    print(lista[c], end=' ')
