print('{}='.format('\033[34m') * 54)
print('{:=^54}'.format(' Gerenciador de Pagamentos '))
print('=' * 54)
p = float(input('{}Preço das compras: R$'.format('\033[33m')))
print('''{}FORMAS DE PAGAMENTO
[ 1 ] á vista no dinheiro/cheque com 10% de desconto
[ 2 ] á vista no cartão com 5% de desconto
[ 3 ] 2x no cartão sem desconto
[ 4 ] 3x ou mais no cartão com 20% de juros'''.format('\033[34m'))
f = int(input('{}Sua opção: '.format('\033[33m')))
if f == 1:
    total = p - (p * 10 / 100)
    print('{}R${:.2f} á vista no dinheiro/cheque sairá por R${:.2f}.'.format('\033[36m', p, total))
elif f == 2:
    total = p - (p * 5 / 100)
    print('{}R${:.2f} á vista no cartão sairá por R${:.2f}.'.format('\033[36m', p, total))
elif f == 3:
    total = p
    print('{}R${:.2f} em 2x cada parcela será de R${:.2f} SEM JUROS.'.format('\033[36m', p, p / 2))
elif f == 4:
    v = int(input('Quantas parcelas? '))
    total = p + (p * 20 / 100)
    print('{}Sua compra de R${:.2f} será parcelada em {}x de R${:.2f} COM JUROS.'.format('\033[36m', p, v, total / v))
else:
    total = p
    print('{}Opção Inválida.'.format('\033[31m'))
print('{}Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format('\033[36m', p, total))
