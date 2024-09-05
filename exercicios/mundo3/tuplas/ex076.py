# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma de tabular.
print(20*"=-")
print(f"{"Lista de produtos":^40}".upper())
print(20*"=-")

lista = ("cafe", 5,
         "suco", 3,
         "chá", 7,
         "abacaxi", 12.21)

for item in range (0, len(lista)):
    if item % 2 == 0:
        print(f"{lista[item]:.<29}", end= "")
    else:
        print(f"R${lista[item]:>9.2f}")