# Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros.

medida = float(input("Determine um valor em metros: "))
cm = medida * 100
mm = medida * 1000

print(f"{medida} metros equivalem a:\n{cm} centímetros \n{mm} milímetros")