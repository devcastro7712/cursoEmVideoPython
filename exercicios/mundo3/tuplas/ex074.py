# Crie um programa que vai gerar 5 números aleatórios e vai colocar em uma tupla.
# Depois disso mostre a listagem dos números gerados e também indique qual foi o menor e o maior valor que estão na tupla.
import random

count = 0
numeros = tuple(random.randint(1, 10) for i in range(5))
print(f"Foram sorteados os números: {numeros}")
print(f"O menor valor é: {min(numeros)}")
print(f"O maior valor é: {max(numeros)}")