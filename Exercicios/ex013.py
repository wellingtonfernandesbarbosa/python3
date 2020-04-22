cor = {'limpa':   '\033[m',
       'azul':    '\033[34m',
       'amarelo': '\033[33m',
       'verde':   '\033[32m'}
s = float(input('{}Digite o valor do salário: R$ '.format(cor['azul'])))
a = float(input('Qual a porcentagem do aumento? {}'.format(cor['limpa'])))
ns = s + (s*a/100)
print('O novo salário com aumento de {}{}%{} é de {}R$ {:.2f}{}.'.format(cor['amarelo'], a, cor['limpa'], cor['verde'], ns, cor['verde']))
