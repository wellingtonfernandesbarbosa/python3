print('-=-' * 12)
print('Analisador de Triângulos')
print('-=-' * 12)
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos acima \033[32mPODEM\033[m formar um triângulo.')
else:
    print('Os segmentos acima \033[31mNÃO PODEM\033[m formar um triângulo')
