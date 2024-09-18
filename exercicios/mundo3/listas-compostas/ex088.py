# Crie um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
# entre 1 e 60. Para cada jogo, cadastrando tudo em uma lista composta.
import random

jogos = []

qtd = int(input("Quantos jogos você quer gerar? "))
for i in range(qtd):
    numeros_sorteados = random.sample(range(1, 61), 6)
    jogos.append(numeros_sorteados)

print(f"Foram gerados {qtd} jogos, e são eles: ", end="")
print(jogos)

