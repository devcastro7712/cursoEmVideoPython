# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar , desconsidere-o.
somar_numeros = 0
for i in range(0, 6):
    numero = int(input("Determine um número: "))
    if numero % 2 == 0:
        somar_numeros += numero

print(f"A soma dos valores pares deu {somar_numeros}")