print('-' * 40)
print('{:^40}'.format('LOJA WJ CONECT'))
print('-' * 40)
preco = c = menor = total = 0
pmenor = ' '
while True:
    produto = str(input('Nome do produto: ')).capitalize()
    preco = float(input('Preço: R$ '))
    pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if menor == 0:
        menor = preco
    total += preco
    if preco > 1000:
        c += 1
    if menor >= preco:
        menor = preco
        pmenor = produto
    if pergunta in 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi de R$ {total}')
print(f'Temos {c} produtos custando mais de R$ 1000,00.')
print(f'O produto mais barato foi {pmenor} que custa R$ {menor}')
