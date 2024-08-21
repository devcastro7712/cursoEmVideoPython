# Crie um programa que leia um número real qualquer no teclado, e mostre na tela sua parte inteira.
import math

num = float(input("Digite um número "))
num_int = math.floor(num)
print(f"O inteiro de {num} é {num_int}")