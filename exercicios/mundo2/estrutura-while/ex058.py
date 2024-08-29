# Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora vai tentar adivinhar até acertar.
# Mostrando no final quantos palpites foram nescessários para vencer.

import random

numero = int(input("Digite um número: "))
opcoes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sorteado = random.choice(opcoes)
qtd_numeros_sorteados = 0

while numero != sorteado:
    print(f"Eu escolhi o número {sorteado}")
    numero = int(input("Você errou, digite mais um número: "))
    sorteado = random.choice(opcoes)
    qtd_numeros_sorteados += 1

if numero == sorteado:
    print("Você acertou!")
    print(f"Foram necessárias {qtd_numeros_sorteados + 1} tentativas para me vencer!")


