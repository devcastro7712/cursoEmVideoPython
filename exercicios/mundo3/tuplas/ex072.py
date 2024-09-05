# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado entre (0 e 20) e mostrá-lo por extenso.

numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito",
           "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

numero = int(input("Digite um número entre 0 e 20: "))
while True:
    if 0 < numero < 21:
        print(f"O número {numero} se escreve {numeros[numero]}")
        break
    else:
        numero = int(input("Tente novamente, digite um número de 0 a 20: "))

print("Programa finalizado!")
