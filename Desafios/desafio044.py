p = float(input('Qual o valor do produto: '))
print('Qual a forma de pagamento?')
print('[ 1 ] á vista no dinheiro/cheque com 10% de desconto\n'
      '[ 2 ] á vista no cartão com 5% de desconto\n'
      '[ 3 ] em até 2x no cartão sem desconto\n'
      '[ 4 ] 3x ou mais no cartão com 20% de juros')
f = int(input('Sua opção: '))
if f == 1:
    print('{:.2f} á vista no dinheiro/cheque sairá por R${:.2f}.'.format(p, p - (p * 10 / 100)))
elif f == 2:
    print('R${:.2f} á vista no cartão sairá por R${:.2f}.'.format(p, p - (p * 5 / 100)))
elif f == 3:
    print('R${:.2f} em 2x cada parcela será de R${:.2f}.'.format(p, p / 2))
elif f == 4:
    v = int(input('Quantas parcelas? '))
    print('R${:.2f} em {}x cada parcela será de R${:.2f}.'.format(p, v, (p + (p * 20 / 100)) / v))
else:
    print('Opção Inválida.')
