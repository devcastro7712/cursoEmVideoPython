# Aprimore o desafio anterior mostrando no final:
# A soma de todos os valores pares digitados.
# A soma dos valores da terceira coluna.
# O maior valor da segunda linha.

matriz = [[], [], []]
soma_pares = 0
soma_terceira_coluna = 0
maior_segunda_linha = 0

for linha in range(3):
    for coluna in range(3):
        n = int(input(f'Digite um valor para a posição [{linha}, {coluna}]: '))
        matriz[linha].append(n)

        if n % 2 == 0:
            soma_pares += n
        if coluna == 2:
            soma_terceira_coluna += n
        if linha == 1:
            if coluna == 0:
                maior_segunda_linha = n
            elif n > maior_segunda_linha:
                maior_segunda_linha = n

print("\nMatriz:")
for linha in matriz:
    for valor in linha:
        print(f"[ {valor} ]", end=" ")
    print()
print(f"\nSoma dos valores pares: {soma_pares}")
print(f"Soma dos valores da terceira coluna: {soma_terceira_coluna}")
print(f"Maior valor da segunda linha: {maior_segunda_linha}")