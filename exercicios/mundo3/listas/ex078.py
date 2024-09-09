# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []
for p, i in enumerate(range(0, 5)):
    valor = int(input(f"Digite um valor para a posição {p}: "))
    lista.append(valor)
print(f"A lista é composta pelos valores {lista}")
print(f"O menor valor da lista foi: {min(lista)} e o maior valor da lista foi: {max(lista)}")
