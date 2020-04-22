pessoas = {'nome': 'Wellington', 'sexo': 'M', 'idade': 27}
print(pessoas["nome"])
print(pessoas["sexo"])
print(pessoas["idade"])
print(pessoas.keys())  # Mostra o identificador no dicionário
print(pessoas.values())  # Mostra o conteúdo no dicionário
print(pessoas.items())  # Mostra identificadores e conteúdos no dicionário
pessoas['cor'] = 'Pardo'
for k, v in pessoas.items():  # Nesse caso o .items substitui o enumerate
    print(f'{k} = {v}')
