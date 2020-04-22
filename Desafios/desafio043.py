p = float(input('Digite o peso da pessoa: '))
a = float(input('Digite a altura da pessoa: '))
imc = p / a**2
if imc < 18.5:
    print('Abaixo do Peso')
elif 18.5 <= imc <= 25:
    print('Peso ideal')
elif 25 < imc <= 30:
    print('Sobrepeso')
elif 30 < imc <= 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
