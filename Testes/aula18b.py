galera = list()
dado = list()
maior = menor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        menor += 1
if menor == 1 and maior == 1:
    print(f'Temos {menor} menor e {maior} maior de idade.')
elif menor == 1:
    print(f'Temos {menor} menor e {maior} maiores de idade.')
elif maior == 1:
    print(f'Temos {menor} menores e {maior} maior de idade.')
else:
    print(f'Temos {menor} menores e {maior} maiores de idade.')
