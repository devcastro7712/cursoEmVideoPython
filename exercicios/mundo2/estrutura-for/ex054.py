# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maior idade
# e quantas já são de maior.
import datetime

ano_atual = datetime.date.today().year
ano_de_nascimento = 0
menor_de_idade = 0
maior_de_idade = 0

for pessoa in range(0, 7):
    ano_de_nascimento = int(input("Digite seu ano de nascimento: "))

    if ano_atual - ano_de_nascimento < 18:
        menor_de_idade += 1
    else:
        maior_de_idade += 1


print(f"{maior_de_idade} pessoas já atingiram a maior idade e {menor_de_idade} ainda são menores de idade!")