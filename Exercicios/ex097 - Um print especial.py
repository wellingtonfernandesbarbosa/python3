def título(txt):
    c = len(txt) + 6
    print('=' * c)
    print(f'   {txt}   ')
    print('=' * c)


título(str(input('Digite um título: ')))
