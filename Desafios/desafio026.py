frase = str(input('Escreva uma frase: ')).strip().lower()
print('A letra "a" aparece {} vezes.'.format(frase.count('a')))
print('A posição da primeira letra "a" é {}.'.format(frase.find('a')+1))
print('A posição da última letra "a" é {}.'.format(frase.rfind('a')+1))
