# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.


num = int(input("Digite um número: "))
razao = int(input("Digite uma PA: "))
decimo = num + (10 - 1) * razao
print("Os termos são:")
for i in range(num, decimo, razao):
    print(i)
