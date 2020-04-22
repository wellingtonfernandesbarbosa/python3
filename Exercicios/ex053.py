frase = str(input('Digite uma frase: ')).strip().upper().split()
junto = ''.join(frase)
inverso = junto[::-1]
print('O inverso de {} é {}.'.format(junto, inverso))
if junto == inverso:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo')
