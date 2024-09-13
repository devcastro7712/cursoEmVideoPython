# Crie um programa onde o usuário possa usar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

lista = list()
par = list()
impar = list()
for i in range(0, 7):
    valor = int(input("Determine um valor: "))

    lista.append(valor)
print(f"A lista é composta pelos seguintes valores: {lista}\n")
for numero in lista:
    if numero % 2 == 0:
        par.append(numero)
        par.sort(reverse=True)
    else:
        impar.append(numero)
        impar.sort(reverse=True)
print(f"Os valores pares de forma decrescente são: {par}")
print(f"Os valores ímpares de forma decrescente são: {impar}")