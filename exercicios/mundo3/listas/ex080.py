# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastra-los em uma posição da lista, já na posição correta de inserção
# OBS: (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

lista = []

for i in range(0,5):
    add_valor = int(input("Digite um valor para adicionar a lista: "))
    if not lista:
        lista.append(add_valor)
        print("Primeiro valor adicionado")
    elif add_valor < lista[0]:
        lista.insert(0, add_valor)
        print("O valor foi adicionado a posição 0")
    elif add_valor > lista[-1]:
        lista.append(add_valor)
        print("Valor adicionado no fim da lista")
    else:
        pos = 0
        while pos < len(lista):
            if add_valor <= lista[pos]:
                lista.insert(pos, add_valor)
                print(f"Valor adicionado na posição {pos}")
                break
            pos += 1
print(lista)