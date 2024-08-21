# Crie um programa que leia o nome de uma pessoa e diga se ela tem silva no nome.
nome = input("Digite um nome: ").lower()
if nome.find("silva") < 0:
    print("Não há a palavra silva em sem nome!")
else:
    print("Você tem silva no nome!")