# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final. Mostre:
# Quantas pessoas tem mais de 18 anos.
# Quantos homens foram cadastrados.
# Quantas mulheres tem menos de 20 anos.

maior_de_18 = 0
homens = 0
mulheres_menores_de_20 = 0

while True:
    idade = int(input("Qual a sua idade: "))
    sexo = str(input("Qual o seu sexo [M/F]: ")).upper().strip()[0]

    if idade > 18:
        maior_de_18 += 1

    if sexo == "M":
        homens += 1

    if sexo == "F" and idade < 20:
        mulheres_menores_de_20 += 1

    stop = str(input("Gostaria de adicionar mais uma pessoa [S/N]: ")).upper().strip()[0]
    if stop != "S":
        break
print(homens)

