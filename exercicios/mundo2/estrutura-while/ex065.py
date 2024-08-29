# Crie um programa que leia vários números inteiros pelo teclado, no final da execução mostre a média entre todos os valores e qual foi o maior e o menor valor lidos.
# O programa deve perguntar ao usuário se ele quer parar ou continuar  a digitar valores.

numero = int(input("Digite um número: "))
soma = numero
valores = 1
maior = numero
menor = numero

while True:
    init = input("Deseja adicionar mais um número? [S/N]: ").strip().lower()
    if init != 's':
        break

    numero = int(input("Digite mais um número: "))
    soma += numero
    valores += 1

    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

media = soma / valores

print(f"\nVocê digitou {valores} números.")
print(f"A média entre os valores foi {media:.2f}")
print(f"O maior valor digitado foi {maior}")
print(f"O menor valor digitado foi {menor}")
print("Programa finalizado!")