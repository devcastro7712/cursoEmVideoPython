# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
import random
sortear = random.randint(0, 5)
escolha = int(input("Escolha um número de 0 a 5\n"))


if escolha == sortear:
    print(f"Parabéns você acertou, eu escolhi o número {escolha}")
else:
    print("Você errou, tente novamente!")