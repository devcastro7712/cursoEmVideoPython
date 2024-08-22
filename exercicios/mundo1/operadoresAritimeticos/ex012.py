# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco_produto = float(input("Determine o preço do produto: R$"))
novo_preco_produto = preco_produto - (preco_produto * 5/100)
print(f"O produto custava R${preco_produto:.2f}, com o desconto de 5% passou a custar R${novo_preco_produto:.2f}")
