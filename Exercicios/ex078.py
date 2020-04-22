num = list()
for c in range(0, 5):
    num.append(int(input(f'Digite um valor para a posição {c}: ')))
min = min(num)
max = max(num)
print('Você digitou os valores:', num)
print(f'O menor valor foi {min} nas posições: ', end='')
for i, v in enumerate(num):
    if v == min:
        print(f'{v}...', end='')
print()
print(f'O menor valor foi {min} nas posições: ', end='')
for i, v in enumerate(num):
    if v == max:
        print(f'{v}...', end='')
print()
