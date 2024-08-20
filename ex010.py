# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ele pode comprar.
# Considere = US$1,00 = R$3,27

saldo = float(input("Quanto você tem na carteira: "))
conversao = saldo / 3.27

print(f"seu saldo de R${saldo} vale US${conversao:.2f}")