# Escreva um programa que escreva um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma sequência de fibonacci.
# EX: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

n = int(input("Quantos termos da sequência de Fibonacci você quer ver? "))
a = 0
b = 1
count = 0
print("Sequência de Fibonacci:")
while count < n:
    print(a)
    proximo = a + b
    a = b
    b = proximo
    count += 1