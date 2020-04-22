sexo = ' '
while sexo not in 'MF':
    sexo = str(input('Qual o seu sexo [M/F]? ')).upper().strip()[0]
    if sexo not in 'MF':
        print('Sexo inválido, digite novamente.')
