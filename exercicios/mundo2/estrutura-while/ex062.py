# Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais termos. O programa encerra quanto ele disser que quer mostrar 0 termos.

primeiro_termo = int(input("Qual o primeiro termo: "))
razao = int(input("Qual a razão: "))
termo = primeiro_termo
contador = 1

print(primeiro_termo)
while contador < 10:
    termo += razao
    contador += 1
    print(termo)

while True:
    mais_termos = int(input("Quantos termos mais você quer mostrar? (Digite 0 para encerrar): "))
    if mais_termos == 0:
        break
    contador = 0
    while contador < mais_termos:
        termo += razao
        contador += 1
        print(termo)

print("Fim")