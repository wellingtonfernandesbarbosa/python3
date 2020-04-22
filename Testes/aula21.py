def somar(*num):  # *núm nesse parâmetro indica que pode se atribuir quantos números forem necessários. Os numeros
    # são tranformados em uma tupla para que seja tratado dentro da função
    """
Função para somar números.
Independente da quantidade de termos disponíveis.
	"""
    global a  # Parâmetro para que as mudanças sejam aplicáveis á variável global
    a = 7
    s = 0
    for c in num:
        s += c
    print(f'A soma dos valores é igual a {s}.')
    print()


a = 9
somar(5, 4, 18, 88)
help(somar)
print(somar.__doc__)
print(a)
