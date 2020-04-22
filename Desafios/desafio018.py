import math
v = float(input('Digite um ângulo: '))
s = math.sin(v)
c = math.cos(v)
t = math.tan(v)
print('O valor {}º corresponde aos valores: \nSeno {:.3f} \nCosseno {:.3f} \nTangente {:.3f}'.format(v, s, c, t))
