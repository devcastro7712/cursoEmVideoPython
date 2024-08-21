# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece pela primeira vez.
# Em qual posição ela aparece a última vez.

nome = input("Digite um nome: ").lower()
print(f"Nesse nome, a letra A aparece {nome.count("a")} vezes")
print(f"A letra A aparece pela ultima vez na posição {nome.rfind("a")}")