num = list()
for c in range(0, 5):
    num.append(int(input(f'Digite o {c + 1}º valor: ')))
print('Você digitou os valores:', end='')
min = min(num)
max = max(num)
for c in range(0, len(num)):
    print(f' {num[c]}', end='')
print(f'.\nO menor valor é {min} nas posições: ', end='')
for c in range(0, len(num)):
    if min == num[c]:
        print(f'{c + 1}...', end='')
print(f'\nO maior valor é {max} nas posições: ', end='')
for c in range(0, len(num)):
    if max == num[c]:
        print(f'{c + 1}...', end='')
