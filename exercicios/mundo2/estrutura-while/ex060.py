# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# EX: 5! = 5x4x3x2x1 = 120

numero = int(input("Determine um número: "))
fatorial = 1
contador = numero

while contador > 0:
    fatorial *= contador
    contador -= 1
print(f"O fatorial de {numero} é {fatorial}")