def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(lst)


lista = [8, 7, 9, 4, 8, 1]
dobra(lista)
