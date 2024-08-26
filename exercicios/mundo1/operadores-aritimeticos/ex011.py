# Faça um programa que leia a largura e a altura de uma parade em metros, calcule a sua área e a quantidade de tinta necessária
# para pintá-la, sabendo que cada litros de tinta, pinta uma área de 2m2.

largura = float(input("Qual a largura da parede?"))
altura = float(input("Qual a altura da parede?"))
area = largura * altura
qtd_tinta = area / 2

print(f"para pintar uma parede com uma área de {area}m2, serão necessários {qtd_tinta} litros de tinta")
