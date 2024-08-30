# Faça um programa que jogue par ou impar com o computador.
# O jogador só poderá interromper quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random

print(20 * "=-")
print("Vamos jogar PAR ou ÍMPAR".upper())
print(20 * "=-")
cont_vitorias = 0
while True:
    numero = int(input("\nDigite um valor: "))
    escolha = str(input("Par ou Ímpar [P/I]: ")).upper().strip()[0]
    while escolha not in ["P", "I"]:
        escolha = str(input("Escolha inválida! Par ou Ímpar [P/I]: ")).upper().strip()[0]
    computador = random.randint(0, 10)
    soma = computador + numero
    if soma % 2 == 0:
        resultado = "P"
    else:
        resultado = "I"
    print(f"Você jogou {numero} e o computador jogou {computador}. A soma é {soma}. ", end="")
    print("Deu PAR!" if resultado == "P" else "Deu ÍMPAR!")
    if escolha == resultado:
        print("Você venceu!\n")
        cont_vitorias += 1
    else:
        print("Você perdeu!")
        break
print(f"Fim de jogo! Você teve {cont_vitorias} vitórias consecutivas.")


