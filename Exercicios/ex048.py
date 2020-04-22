s = 0
v = 0
for c in range(1, 500 + 1):
    if c % 2 == 1 and c % 3 == 0:
        r = c / 3
        s += c
        v += 1
print('A soma de todos os {} valores é {}'.format(v, s))
