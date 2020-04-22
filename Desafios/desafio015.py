d = int(input('Quantos dias de aluguel: '))
km = float(input('Quantos quilômetros foram percorridos: '))
v = (d*60) + (km*0.15)
print('Um carro alugado por {} dias e com {}km percorridos terá o valor final do aluguel de R${:.2f}.'.format(d, km, v))
