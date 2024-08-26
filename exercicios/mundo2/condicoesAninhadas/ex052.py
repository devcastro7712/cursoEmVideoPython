# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input("Digite um número: "))
total = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        total += 1
        print(total)
print(f"O número {numero} foi divisível {total} vezes")

if total == 2:
    print("Por isso é um número primo")
else:
    print("Por isso não é um número primo")