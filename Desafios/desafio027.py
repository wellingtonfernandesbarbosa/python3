n = str(input('Digite o seu nome: ')).strip().title()
nome = n.split()
u = len(nome)-1
print('Primeiro nome: {}'.format(nome[0]))
print('Último nome: {}'.format(nome[u]))
