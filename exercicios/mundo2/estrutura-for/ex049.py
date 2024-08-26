# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço for.

num = int(input("Digite um número: "))
for i in range(1, 10):
    r = num * i
    print(f"{num} x {i} = {r}")
