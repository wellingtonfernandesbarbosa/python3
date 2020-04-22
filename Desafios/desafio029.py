v = float(input('Qual a velocidade do carro? '))
if v < 80:
    print('Você está dentro do limite de velocidade!')
    if v < 55:
        print('Você está abaixo do limite mínimo de velocidade, CUIDADO!')
else:
    print('Você está acima do limite de velocidade, e sua multa será de R${:.2f}.'.format((v-80) * 7))
