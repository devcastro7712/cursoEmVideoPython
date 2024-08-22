# O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos alunos, faça um programa que leia o nome dos quatro
# Alunos e mostre a ordem sorteada.
import random

alunos = ["Lucas", "Gaby", "Loly", "Kenai"]
random.shuffle(alunos)
print(alunos)