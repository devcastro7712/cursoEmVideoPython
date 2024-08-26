# Crie um algoritimo que leia um número e mostre seu dobro, triplo e raiz
import math

num = int(input("Digite um numero"))
db = num * 2
tri = num * 3
raiz = math.sqrt(num)

print(f"O dobro de {num} é {db}, o triplo é {tri} e a raiz quadrada é {raiz}")