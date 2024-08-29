# Crie um programa que leia vários números inteiros pelo teclado, o programa só vai parar quando digitar o número 999, que é a condição de parada
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
print(30*"=-")
print("bem vindo ao programa de leitura e soma de números".title())
init = str(input("Você quer iniciar o programa? [s/n]: "))
numero = 0
soma = numero
qtd_numeros = 0
if init == "s":
    while numero != 999:
        numero = int(input("Digite um número: "))
        soma = soma + numero
        qtd_numeros += 1
    print(f"Foram somados {qtd_numeros - 1} números, e a soma resultou no número {soma - 999}")
else:
    print("\nOk, obrigado por entrar em nosso programa!")
