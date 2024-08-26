# Desenvolva um programa que leia o comprimeiro de três retas e diga ao usuário
# Se ele pode ou não formar um triÂngulo

a = int(input("Determine o tamanho de uma reta: "))
b = int(input("Determine o tamanho de uma reta: "))
c = int(input("Determine o tamanho de uma reta: "))

if a + b > c and b + c > a and a + c > b:
    print("As três retas formam um triângulo!")
else:
    print("Infelizmente não é possível formar um triângulo com os valores que você me ofereceu")