from random import randint

p = j = t = 0
ej = ' '
print('=' * 24)
print('VAMOS JOGAR PAR IU IMPAR')
print('=' * 24)
while True:
    nj = int(input('Diga um número: '))
    while ej not in 'PI':
        ej = str(input('Par ou impar? [P/I] ')).strip().upper()[0]
    nc = randint(0, 11)
    t = nj + nc
    if t % 2 == 0 and ej in 'P':
        print(f'VOCÊ GANHOU! Voce jogou {nj} e o computador {nc}. Total de {t} deu PAR')
        p += 1
    elif t % 2 != 0 and ej in 'I':
        print(f'VOCÊ GANHOU! Voce jogou {nj} e o computador {nc}. Total de {t} deu IMPAR')
    elif t % 2 == 0 and ej in 'I':
        print(f'VOCÊ PERDEU! Voce jogou {nj} e o computador {nc}. Total de {t} deu PAR')
        p += 1
        break
    elif t % 2 != 0 and ej in 'P':
        print(f'VOCÊ PERDEU! Voce jogou {nj} e o computador {nc}. Total de {t} deu IMPAR')
        break
    j += 1
print('=' * 64)
if j == 1:
    print(f'GAME OVER! Você venceu {j} vez.')
else:
    print(f'GAME OVER! Você venceu {j} vezes.')
