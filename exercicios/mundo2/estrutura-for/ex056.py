# Desenvolva um programa que leia nome, idade e sexo de 4 pessoas. No final do programa mostre:
# A média de idade do grupo.
# Qual o nome do homem mais velho.
# Quantas mulheres tem menos de 20 anos.

soma_de_idades = 0
nome_mais_velho = ""
idade_homem_mais_velho = 0
mulheres_menores_20 = 0

for pessoa in range(1, 5):
    nome = input(f"Digite o nome da {pessoa}° pessoa: ").upper().strip()
    idade = int(input(f"Digite a idade da {pessoa}° pessoa: "))
    sexo = input(f"Digite o sexo da {pessoa} pessoa: (m ou f) ").upper().strip()

    soma_de_idades += idade

    if pessoa == 1 and sexo == "M":
        idade_homem_mais_velho = idade
        nome_mais_velho = nome

    if sexo == "M" and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_mais_velho = nome

    if sexo == "F" and idade < 20:
        mulheres_menores_20 += 1

media_De_idade = int(soma_de_idades / 4)

print(50 * "=")
print(f"\nA média de idade do grupo é de {media_De_idade} anos\n")
print(f"O homem com a maior idade tem {idade_homem_mais_velho} anos e se chama {nome_mais_velho}\n")
print(f"Existe(m) {mulheres_menores_20} mulher(es) menor(es) de 20 anos!")

