print('=' * 42)
print('{:^42}'.format('LOJA WJ CONECT'))
print('=' * 42)
t = c = menor = tmil = 0
pmenor = ' '
while True:
    produto = str(input('Nome do produto: ')).upper().capitalize()
    preco = float(input('Preço: R$ '))
    r = ' '
    t += preco
    c += 1
    if preco > 1000:
        tmil += 1
    if c == 1 or preco < menor:
        menor = preco
        pmenor = produto
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('{:-^42}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi de R$ {t:.2f}')
if tmil == 1:
    print(f'Temos 1 produto custando mais de R$ 1.000,00')
elif tmil > 1:
    print(f'Temos {tmil} produtos custando mais de R$ 1.000,00')
print(f'O produto mais barato foi {pmenor} que custa R$ {menor:.2f}')
