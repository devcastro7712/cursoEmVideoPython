# Desenvolva um programa que leia 4 valores pelo teclado e guardar numa tupla, no final mostre:
# Quantas vezes apareceu o valor 9.
# Em que posição foi digitado o primeiro valor 3.
# Quais foram os números pares.
count = 0
numeros = []
numeros_9 = 0
numeros_pares = []
while count < 5:
    numeros.append(int(input("Adicione um número: ")))
    count += 1
numeros = tuple(numeros)

for valor in numeros:
    if valor == 9:
        numeros_9 += 1
    if valor % 2 == 0:
        numeros_pares.append(valor)
numeros_pares = tuple(numeros_pares)

print(20*"=-")
print(f"\nVocê gerou uma tupla com os valores: {numeros}")
print(f"Foram gerados {numeros_9} numeros 9")
print(f"O número 3 foi digitado inicialmente na posição {numeros.index(3)}")
print(f"Os números pares da tupla são: {numeros_pares}")

