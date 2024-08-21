# Faça um programa que leia o comprimeiro do cateto oposto e do cateto adjascente de um triângulo retângulo, calcule e mostre
# o comprimento da hipotenusa
import math
cat_o = float(input("Qual o cateto oposto? "))
cat_a = float(input("Qual o cateto adjascente? "))
hip = math.hypot(cat_o, cat_a)

print(f"a hipotenusa é: {hip:.2f}")