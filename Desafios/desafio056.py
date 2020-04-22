media = 0
c = 0
ihv = 0
homem = ' '
for p in range(1, 5):
    print('----- {}ª Pessoa -----'.format(p))
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    media += idade
    if p == 1 and sexo == 'M':
        ihv = idade
        homem = nome
    if sexo == 'M' and idade > ihv:
        ihv = idade
        homem = nome
    if sexo == 'F' and idade < 20:
        c += 1
print('A média de idade do grupo é de {} anos.'.format(media / 4))
print('O homem mais velho do grupo tem {} anos e se chama {}.'.format(ihv, homem))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(c))
