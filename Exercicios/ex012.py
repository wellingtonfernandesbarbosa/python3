cor = {'limpa': '\033[m',
       'azul': '\033[34m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'lilás': '\033[35m'}
p = float(input('{}Qual o preço do produto? R$ '.format(cor['lilás'])))
d = float(input('Qual a porcentagem do desconto? {}'.format(cor['limpa'])))
np = p - (p * d/100)
print('O produto que custava {}R$ {}{}, na promoção com desconto de {}{}%{} vai custar {}R$ {:.3f}{}.'.format(cor['azul'], p, cor['limpa'], cor['amarelo'], d, cor['limpa'], cor['verde'], np, cor['limpa']))
