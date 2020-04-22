s = float(input('Digite o valor do salário: R$'))
if s > 1250:
    print('O salário terá um almento de 10% e o novo valor será de R${:.2f}'.format(s * 1.10))
else:
    print('O salário terá um almento de 15% e o novo valor será de R${:.2f}'.format(s * 1.15))
