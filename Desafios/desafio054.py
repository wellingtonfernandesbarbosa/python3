from datetime import date
maior = 0
menor = 0
for c in range(1, 7 + 1):
    n = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    i = date.today().year - n
    if i < 21:
        menor += 1
    else:
        maior += 1
print('Ao todo tivemos {} pessoas menores de idade.'.format(menor))
print('E também tivemos {} pessoas maiores de idade.'.format(maior))
