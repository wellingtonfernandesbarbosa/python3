lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
lanche[3] = 'batata'
lanche.append('cookie')  # Para adicionar um elemente ao final da lista
lanche.insert(3, 'picolé')  # Para adicionar um elemento na osição indicada. lembrando que dessa forma a lista aumenta
del lanche[2]  # Para apagar o elemento indicado pela posição 3
lanche.pop(0)  # Normalmente utilizado para apagar o último elemento,
# também pode ser utilizado para apagar outros elementos
lanche.remove('suco')  # Também utilixado para apagar, mas através da declaração do item a ser apagado
for c in lanche:
    print(c.capitalize())
valores = list(range(7, 21))  # Declaração de lista através do camando list
print(valores)
valor = [8, 2, 5, 4, 9, 3, 0]
print(valor)
valor.sort()  # Altera de forma definitiva a ordem dos valores, colocando tudo em ordem crescente
print(valor)
valor.sort(reverse=True)  # Altera de forma definitiva a ordem dos valores, colocando tudo em ordem decrescente
print(valor)
