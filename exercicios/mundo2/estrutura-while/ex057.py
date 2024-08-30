# Faça um programa que leia o sexo de uma pessoa mais so aceite M ou F, caso esteja errado. Peça a digitação novamente até que esteja certo.

sexo = "m"

while True:
    sexo = input("Digite seu sexo [M ou F]: ").lower()[0].strip()
    if sexo != "m" and sexo != "f":
        print("Opção errada, digite novamente!")
    else:
        print(f"Obrigado!")
        break

