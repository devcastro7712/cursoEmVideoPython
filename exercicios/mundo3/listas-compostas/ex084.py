# Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista, no final vai mostrar:
# Quantas pessoas foram cadastradas.
# Uma lista com as pessoas mais pesadas.
# Uma lista com as pessoas mais leves.

lista = []
mais_pesada = pessoas_cadastradas = 0
mais_leve = float("inf")
lMaisPesada = []
lMaisLeve = []
while True:
    nome = str(input("Qual o nome: "))
    peso = float(input("Qual o peso: "))
    lista.append([nome, peso])
    pessoas_cadastradas += 1

    if peso > mais_pesada:
        mais_pesada = peso
        lMaisPesada = [nome]
    elif peso == mais_pesada:
        lMaisPesada.append(nome)

    if peso < mais_leve:
        mais_leve = peso
        lMaisLeve = [nome]
    elif peso == mais_leve:
        lMaisLeve.append(nome)

    init = str(input("Adicionar outra pessoa? [S/N]: ")).upper().strip()[0]
    if init == "N":
        break
print(f"\nTotal de pessoas cadastradas: {pessoas_cadastradas}")
print(f"Pessoa(s) mais pesada(s) ({mais_pesada} Kg):")

for pessoa in lMaisPesada:
    print(f"- {pessoa}")
print(f"Pessoa(s) mais leve(s) ({mais_leve} Kg):")
for pessoa in lMaisLeve:
    print(f"- {pessoa}")