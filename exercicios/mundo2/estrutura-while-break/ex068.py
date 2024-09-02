# Faça um programa que jogue par ou impar com o computador.
# O jogador só poderá interromper quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random

total_de_vitorias = 0
while True:

    escolha_do_usuario_numero = int(input("Escolha um número: "))
    escolha_do_usuario_par_impar = str(input("Você quer par ou ímpar? [P/I]: ")).upper().strip()[0]

    escolha_do_computador_numero = random.randint(0, 10)
    soma = escolha_do_computador_numero + escolha_do_usuario_numero

    if soma % 2 == 0:
        resultado = "P"
    else:
        resultado = "I"

    if escolha_do_usuario_par_impar == resultado:
        print("Você venceu!")
        total_de_vitorias += 1
    else:
        print(f"Você perdeu! O total de vitórias consecutivas foi de {total_de_vitorias}.")
        break

print("Programa finalizado!")