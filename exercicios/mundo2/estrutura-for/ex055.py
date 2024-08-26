# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor pesos lidos.

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input("Digite o peso de uma pessoa: "))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso

print(f"A pessoa com o maior peso tem: {maior}kg")
print(f"A pessoa com o menor peso tem {menor}Kg")
