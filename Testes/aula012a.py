s = 0
v = int(input('Deseja somar quantos números? '))
for c in range(0, v):
    n = int(input('Digite um número: '))
    s += n #alternativa ao comando (s = s + n)
print('A soma dos valores digitados foi: {}'.format(s))
