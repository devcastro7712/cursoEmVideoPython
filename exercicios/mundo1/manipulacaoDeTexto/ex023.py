# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.

num = int(input("Digite um número de até 4 dígitos: "))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print(f"O número {num} tem:\n"
      f"{milhar} milhar\n"
      f"{centena} centenas\n"
      f"{dezena} dezenas\n"
      f"{unidade} unidades")