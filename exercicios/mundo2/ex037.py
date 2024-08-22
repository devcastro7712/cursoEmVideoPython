# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        opcao = int(input("Digite 1 para converter para binário, 2 para octal e 3 para hexadecimal: "))

        if opcao == 1:
            print(f"O número {numero} em binário é: {bin(numero)[2:]}")
            break
        elif opcao == 2:
            print(f"O número {numero} em octal é: {oct(numero)[2:]}")
            break
        elif opcao == 3:
            print(f"O número {numero} em hexadecimal é: {hex(numero)[2:]}")
            break
        else:
            print("Opção inválida, por favor, escolha uma das opções: 1, 2 ou 3.")
    except ValueError:
        print("Entrada inválida! Por favor, digite um número inteiro e escolha uma opção válida.")
