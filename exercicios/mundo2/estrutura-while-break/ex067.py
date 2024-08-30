# Faça um programa que mostre a tabuadade vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:
    numero = int(input("Quer ver a tabuada de qual número? "))
    if numero < 0:
        break

    tabuada = 1
    while tabuada <= 10:
        multiplicacao = numero * tabuada
        print(f"{numero} x {tabuada} = {multiplicacao}")
        tabuada += 1

print("Programa encerrado.")

