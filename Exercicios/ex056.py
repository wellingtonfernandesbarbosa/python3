idademaior = 0
homem = ' '
c = 0
media = 0
for p in range(1, 5):
    print('----- {}ª Pessoa -----'.format(p))
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    if p == 1 and sexo == 'M':
        idademaior = idade
        homem = nome
    if idademaior < idade and sexo == 'M':
        idademaior = idade
        homem = nome
    if idade < 20 and sexo == 'F':
        c += 1
    media += idade
print('A média de idade do grupo é {} anos.'.format(media /4))
print('O homem mais velho do grupo tem {} anos e se chama {}.'.format(idademaior, homem))
if c == 0:
    print('Nao existem mulheres no grupo com menos de 20 anos')
elif c == 1:
    print('Existe 1 mulher no grupo com menos de 20 anos')
elif c > 1:
    print('Ao todo são {} mulheres com menoa de 20 anos'.format(c))
