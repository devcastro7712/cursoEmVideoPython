# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que cada caixa possui cédulas de R$50, R$20, R$10 e R$1.

print("Bem-vindo ao caixa eletrônico!")

valor_saque = int(input("Digite o valor que você deseja sacar: "))

cedulas_50 = 0
cedulas_20 = 0
cedulas_10 = 0
cedulas_1 = 0

cedulas_50 = valor_saque // 50
valor_saque %= 50

cedulas_20 = valor_saque // 20
valor_saque %= 20

cedulas_10 = valor_saque // 10
valor_saque %= 10

cedulas_1 = valor_saque // 1

print("\nVocê receberá:")
if cedulas_50 > 0:
    print(f"{cedulas_50} cédula(s) de R$50")
if cedulas_20 > 0:
    print(f"{cedulas_20} cédula(s) de R$20")
if cedulas_10 > 0:
    print(f"{cedulas_10} cédula(s) de R$10")
if cedulas_1 > 0:
    print(f"{cedulas_1} cédula(s) de R$1")
