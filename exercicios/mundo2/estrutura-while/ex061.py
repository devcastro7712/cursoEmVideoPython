# Refaça o desafio 51, lendo o primeiro termo e a razão de PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro_termo = int(input("Qual o primeiro termo: "))
razao = int(input("Qual a razão: "))
termo = primeiro_termo
contador = 1

print(primeiro_termo)
while contador < 11:
    termo += razao
    contador += 1
    print(termo)

print("fim")