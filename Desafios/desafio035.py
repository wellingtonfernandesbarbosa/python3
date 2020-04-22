n1 = float(input('Digite o 1º valor: '))
n2 = float(input('Digite o 2º valor: '))
n3 = float(input('Digite o 3º valor: '))
if n1 + n2 > n3 and n2 + n3 > n1 and n3 + n1 > n2:
    print('Pode formar um triângulo.')
else:
    print('Não pode formar um triângulo.')
