# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e ímpares digitados respectivamente.
# Ao final mostre o conteúdo das 3 listas geradas.

lista = []
lista_par = []
lista_impar = []

init = str(input("Quer adicionar um valor a lista [S/N]: ")).upper().strip()[0]
while True:
    while init == "S":
        adicionar_valor = int(input("Adicione um valor a lista: "))
        lista.append(adicionar_valor)
        init = str(input("Quer adicionar um valor a lista [S/N]: ")).upper().strip()[0]
        if adicionar_valor % 2 == 0:
            lista_par.append(adicionar_valor)
        else:
            lista_impar.append(adicionar_valor)
    break
lista_par.sort()
lista_impar.sort()
lista.sort()
print("\n")
print(40*"=")
print("leitura finalizada!".upper().center(40))
print(40 * "=")
print(f"Lista geral: {lista}")
print(f"Lista apenas com valores pares: {lista_par}")
print(f"Lista apenas com valores ímpares: {lista_impar}")