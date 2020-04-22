frase = ('Curso em Vídeo Python')

# Análise
print(len(frase))  # Mostrar o tamanho da string
print(frase.count('o', 0, 21))  # Mostrar quantas vezes a letra indicada aparece na string do espaço 0 até o 21
print(frase[7])  # Exemplo do que ocupa a 7º espaço
print(frase[9::3])  # Exemplo para contar do 9º espaço em diante pulando 3 letras
print(frase.count('e'))  # Mostrar quantas vezes a letra indicada aparece na string
print(frase.find('deo'))  # Mostrar em que espaço inicia a palavra ente ''
print('Curso' in frase)  # Para verificar se a paravra entre '' está na string

# Transformação
print(frase.replace('Python', 'Android'))  # Trocar palavras somente nessa instância
frase = frase.replace('Python', 'Android')  # Trocar a palavra permanentemente
print(frase.upper())  # para colocar tudo em maiúsculas
print(frase.lower())  # para colcar tudo em minúsculas
print(frase.capitalize())  # primeira letra da string em maiúscula
print(frase.title())  # primeira letra de cada palavra em minúsculas

frase1 = ('   Aprenda Python  ')
print(frase1.strip())  # para tirar os espaços da string
print(frase1.rstrip())  # para tirar os espaços da direita
print(frase1.lstrip())  # para tirar os espaços da esquerda

# Divisão
print(frase.split())  # O split gera uma lista com todas as palavras de uma cadeia de caracteres
dividido = frase.split()
print(dividido[0])  # Mostrar somente a palavra que começa em 0
print(dividido[3][4])  # Mostrar o caractere do espaço 4 dentro do bloco 3

# Junção
print('-'.join(frase))  # O join colocará o que for designado entre '' no meio de todos os caracteres
