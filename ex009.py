# Escreva um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

num = int(input("Determine um número: "))
tabuada = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in tabuada:
    r = num * i
    print(f"{num} x {i} = {r}")
