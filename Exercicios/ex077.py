lista = ('aprender', 'programar', 'python', 'curso', 'gratis', 'estudar',
         'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for palavra in lista:
    print(f'\nNa palavra {palavra.upper()} temos: ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')
