from random import randint

v = j = 0
print('=' * 24)
print('VAMOS JOGAR PAR OU IMPAR')
print('=' * 24)
while True:
    nj = int(input('Digite um valor: '))
    nc = randint(1, 11)
    t = nj + nc
    ej = ' '
    while ej not in 'PI':
        ej = str(input('Par ou impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {nj} e o computador jogou {nc}. Total de {t}, ', end=' ')
    print('DEU PAR!' if t % 2 == 0 else 'DEU IMPAR!')
    if ej == 'P':
        if t % 2 == 0:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    if ej == "I":
        if t % 2 != 0:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogar novamente...')
if v == 0:
    print('Que pena! Vai deixar o pc te bater tão fácil?')
elif v == 1:
    print(f'Você venceu APENAS {v} vez.')
elif v < 1:
    print(f'GAME OVER! Você venceu {v} vezes.')
