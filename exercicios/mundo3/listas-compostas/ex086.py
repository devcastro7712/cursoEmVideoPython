# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela com a formatação correta.

matriz = [[], [], []]
for linha in range(3):
    for coluna in range(3):
        n = int(input(f'Digite um valor para a posição [{linha}, {coluna}]: '))
        if 0 <= n <= 9:
            matriz[linha].append(n)
        else:
            print("Apenas valores de 0 a 9 são permitidos!")
            break

print("\nMatriz:")
for linha in matriz:
    for valor in linha:
        print(f"[ {valor} ]", end=" ")
    print()