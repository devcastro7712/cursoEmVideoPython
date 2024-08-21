# Crie um programa que leia o nome de uma cidade e ele vai te dizer se a cidade começa ou não com a palavra santo.

cidade = input("Diga o nome de uma cidade: ").lower().strip()
inicialCidade = cidade.split()
if inicialCidade[0] == "santo":
    print("O nome da cidade inicia com santo!")
else:
    print("O nome da cidade não inicia com santos!")


