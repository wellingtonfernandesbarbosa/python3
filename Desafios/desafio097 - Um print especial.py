def escreva(msg):
    t = len(msg) + 4
    print('~' * t)
    print(f'  {msg}  ')
    print('~' * t)


texto = str(input('Escreva um texto: '))
escreva(texto)
