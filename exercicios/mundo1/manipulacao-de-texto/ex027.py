# Faça um programa que leia o nome completo de uma pessoa e mostre em seguida o primeiro e o último nome separadamente.
nome = input("Digite um nome: ").lower().strip()
fatiando = nome.split()
print(f"O primeiro nome é: {fatiando[0]}")
print(f"O ultimo nome é: {fatiando[len(fatiando)-1]}")

