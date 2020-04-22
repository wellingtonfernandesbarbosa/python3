cores = {'limpa' : '\033[m',
	'verde': '\033[32m'}
print('Aumento de salário')
s = float(input('Qual o salário do funcionário: R$ '))
a = 15
if s > 1250:
    a = 10
ns = s + (s * a / 100)
print('Para o salário de R$ {:.2f} o aumento será de {}% e o novo valor será de R$ {}{:.2f}{}.'.format(s, a, cores['verde'], ns, cores['limpa']))