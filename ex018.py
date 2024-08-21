# Faça um programa que leia um ângulo qualquer e mostre na tela seu seno, cosseno e tangente.
import math

angulo = float(input("Me de o valor do ângulo: "))
sin = math.sin(angulo)
cos = math.cos(angulo)
tan = math.tan(angulo)

print(f"você determinou o valor: {angulo}\n"
      f"seu seno é: {sin}\n"
      f"seu cosseno é: {cos}\n"
      f"sua hipotenusa é: {tan}\n")