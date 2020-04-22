a = [3, 8, 7, 9]
b = a  # Quando uma variavel recebe uma lista é criado um elo, em que a alteração na segunda afeta a primeira
c = a[:]  # Se feita dessa forma a variavel c recebe todos os itens, mas sem a ligação
b[2] = 1
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')
