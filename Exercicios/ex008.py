n = float(input('Uma distância em metros: '))
print('{} metros equivalem a: '.format(n))
print('{}{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm{}'.format('\033[34m', (n/1000), (n/100), (n/10), (n*10), (n*100), (n*1000), '\033[m'))
