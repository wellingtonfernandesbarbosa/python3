teste = list()
teste.append('Wellington')
teste.append(27)
galera = list()
galera.append(teste[:])
teste[0] = 'Jacqueline'
teste[1] = 26
galera.append(teste)
print(galera)
