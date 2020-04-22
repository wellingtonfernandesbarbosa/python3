lista = str(input('Digite sua expressão: '))
pilha = []
for simb in lista:
    if simb == '(':
        pilha.append(simb)
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(simb)
            break
if len(pilha) == 0:
    print('Sua expressão está correta.')
else:
    print('Sua expressão está incorreta.')
