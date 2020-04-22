tempo = int(input('Quantos anos tem seu carro: '))
if tempo <= 3:
    print('Seu carro ainda deve estar com cheirinho de novo.')
else:
    print('Carro de meia idade :-), hora de dar uma recauchutada.')

print('Carro novo' if tempo <= 3 else 'Carro velho')
print('---FIM---')
