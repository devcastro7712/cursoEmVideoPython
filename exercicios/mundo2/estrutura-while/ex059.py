# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] Somar
# [2] Multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso.
print(30*"=-")
print("bem-vindo ao programa de manipulação de valores!".upper().title())
valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite um valor: "))

print("\nEscolha o que deseja fazer com os valores!")
print("[1] Somar\n"
      "[2] Multiplicar\n"
      "[3] Maior\n"
      "[4] Novos Números\n"
      "[5] Sair")
escolha = int(input("Qual opção deseja escolher: "))
maior = valor1

while True:
    if escolha == 1:
        print(f"A soma entre os valores é: {valor1 + valor2}")
        break

    elif escolha == 2:
        print(f"A multiplicaçnao entre os valores é: {valor1 * valor2}")
        break

    elif escolha == 3:
        if valor2 > valor1:
            print(f"{valor2} é maior que {valor1}")
            break
        elif valor2 == valor1:
            print("Ambos são iguais!")
            break
        else:
            print(f"{valor1} é maior que {valor2}")
            break

    elif escolha == 4:
        valor1 = int(input("Digite um novo valor para o valor 1: "))
        valor2 = int(input("Digite um novo valor para o valor 2: "))
        print(f"Agora o valor 1 corresponde a: {valor1}\ne o valor 2 a: {valor2}")
        break

    elif escolha == 5:
        print("\nPrograma encerrado!")
        break

    else:
        print("\nOpção inválida, vamos tentar novamente!")
        print("Escolha o que deseja fazer com os valores!")
        print("[1] Somar\n"
              "[2] Multiplicar\n"
              "[3] Maior\n"
              "[4] Novos Números\n"
              "[5] Sair")
        escolha = int(input("Qual opção deseja escolher: "))

print("Obrigado por usar nosso programa!")





