# Faça um programa que leia algo pelo teclado e mostre seu tipo primitivo e todas as informações possíveis sobre ele.
valor = input("Digite um valor")
print(f"{valor} é alfabético?", valor.isalpha())
print(f"{valor} é um número?", valor.isnumeric())
print(f"{valor} é alfanumérico?", valor.isalnum())
print(f"{valor} está em maiusculo?", valor.isupper())
print(f"{valor} é feito de espaços?", valor.isspace())
print(f"{valor} está em menusculo?", valor.islower())
print(f"{valor} está captalizada?", valor.istitle())