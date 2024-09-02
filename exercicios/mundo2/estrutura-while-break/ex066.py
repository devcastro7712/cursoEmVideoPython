# Crie um programa que leia varios números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999 que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

soma = 0
cont = 0
while True:
    num = int(input("Digite um número: "))
    if num != 999:
        soma += num
        cont += 1
    else:
        break

print(f"Foram digitados {cont} números e a soma entre eles foi {soma}")