# Faça um programa que calcule a soma entre todos os números impares que são multiplos de três e que se encontram no intervalo de 1 a 500.

soma = 0
for numero in range(1, 501):
    if numero % 2 != 0 and numero % 3 == 0:
        soma += numero

print(f"A soma de todos os números ímpares múltiplos de três no intervalo de 1 a 500 é: {soma}")