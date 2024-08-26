# Crie um programa que faça o computador jogar jokempô com você!
import random

iniciar = input("Começar a partida? (sim) ou (não)").lower()

try:
    while iniciar == "sim" or iniciar == "s":
        opcoes = random.choice(["pedra", "papel", "tesoura"])
        escolha = input("Você escolhe: pedra, papel, tesoura? ").lower()

        print(f"Eu escolhi: {opcoes}")

        if opcoes == escolha:
            print("Deu empate!")
        elif (opcoes == "pedra" and escolha == "tesoura") or (opcoes == "tesoura" and escolha == "papel") or (
                opcoes == "papel" and escolha == "pedra"):
            print("Eu ganhei!")
        elif (escolha == "pedra" and opcoes == "tesoura") or (escolha == "tesoura" and opcoes == "papel") or (
                escolha == "papel" and opcoes == "pedra"):
            print("Você ganhou!")
        else:
            print("Escolha inválida!")

        retornar = input("Deseja jogar novamente? (sim) ou (não)").lower()

        if retornar != "sim" and retornar != "s":
            print("Jogo finalizado!")
            break

    print("Me procure quando quiser jogar novamente!")

except:
    print("Ocorreu um erro. Volte quando quiser jogar!")

