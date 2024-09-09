# Crie um programa onde o usuário possa digitar vários valores numérios e cadastre-os em uma lista. Caso o número já exista la dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente
lista = []
while True:
    init= str(input("Deseja adicionar um valor [S/N]: ")).upper().strip()[0]
    if init == "S":
        adicionar_valor = int(input("Adicione um valor a lista: "))
        lista.append(adicionar_valor)

    else:
        break
print(lista)