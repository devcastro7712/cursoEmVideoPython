# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e menúsculas.
# Quantas letras ao toddo sem considerar os espaços.
# quantas letras no primeiro nome.

from itertools import count
from re import fullmatch

nome = "erison LucAS DE JeSUS cAstro"
print(f"Seu nome em maiúsculo: {nome.upper()}")
print(f"Seu nome em menúsculo: {nome.lower()}")
print(f"Seu nome tem ao todo {len(nome) - nome.count(" ")} letras sem considerar os espaços")
nomeQuebrado = nome.split()
print(nomeQuebrado[0])