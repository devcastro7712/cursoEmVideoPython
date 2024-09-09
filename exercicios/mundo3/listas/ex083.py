# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parenteses abertos e fechados na ordem correta.

expressao = input("Digite uma expressão com parênteses: ")
pilha = []

correta = True
for char in expressao:
    if char == '(':
        pilha.append('(')
    elif char == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            correta = False
            break
if len(pilha) == 0 and correta:
    print("A expressão está correta!")
else:
    print("A expressão está incorreta!")