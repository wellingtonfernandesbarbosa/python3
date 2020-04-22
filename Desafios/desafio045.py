from random import choice
print('Vamos jogar Jokenpô? ')
e = str(input('Qual você escolhe: pedra, papel ou tesoura: '))
lista = ['pedra', 'papel', 'tesoura']
r = choice(lista)
if r == e:
    print('Empate')
elif r == 'pedra' and e == 'papel':
    print('Voce ganhou')
elif r == 'pedra' and e == 'tesoura':
    print('Você perdeu')
elif r == 'papel' and e == 'pedra':
    print('Você perdeu')
elif r == 'papel' and e == 'tesoura':
    print('Você ganhou')
elif r == 'tesoura' and e == 'pedra':
    print('Você ganhou')
else:
    print('Você perdeu')
