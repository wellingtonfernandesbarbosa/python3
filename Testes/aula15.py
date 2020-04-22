c = 0
while True:
    print(f'{c}', end='')
    if c == 256:
        print('. FIM.')
        break
    c += 1
    print(', ', end='')
