# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# Qual é o total gasto na compra.
# Quantos produtos custam mais de R$1000.
# Qual é o nome do produto mais barato.

total_gasto = 0
acima_de_mil = 0
mais_barato = float("inf")
nome_mais_barato = ""

print(20*"=-")
print("bem vindo a sua lista de compras!".upper())
print("Vamos fazer o balanço das suas compras?\n")

while True:
    nome = str(input("Digite o nome do produto: ")).strip().title()
    preco = float(input("Digite o preço do produto R$"))
    total_gasto += preco

    if preco > 1000:
        acima_de_mil += 1

    if preco < mais_barato:
        mais_barato = preco
        nome_mais_barato = nome

    adicionar = str(input("Deseja adicionar mais itens? [S/N]: ")).upper().strip()[0]
    if adicionar != "S":
        break

print(2*"=-")
print("balanço da compra!".title())

print(f"\n- No total foram gastos R${total_gasto:.2f}")
print(f"- {acima_de_mil} produto(s) custou(aram) mais de R$1000.00")
print(f"- O produto mais barato foi a(o) {nome_mais_barato} e ele custou R${mais_barato:.2f}")