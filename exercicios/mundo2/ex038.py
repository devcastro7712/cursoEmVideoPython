# Escreva um programa que leia dois números inteiro e compare-os, mostrando na tela a mensagem:
# O primeiro valor é maior
# O segundo valor é mairo
# Não existe valor maior, os dois são iguais

valor1 = int(input("Determine um valor: "))
valor2 = int(input("Determine mais um valor: "))

if valor1 > valor2:
    print(f"{valor1} é maior que {valor2}")
elif valor2 > valor1:
    print(f"{valor2} é maior que {valor1}")
else:
    print("Não existe valor maior, ambos os valores são iguais!")