# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados são iguais.
# Isósceles: dois lados iguais.
# Escaleno: Todos os lados diferentes.

a = int(input("Determine o tamanho de uma reta: "))
b = int(input("Determine o tamanho de uma reta: "))
c = int(input("Determine o tamanho de uma reta: "))

if a + b > c and b + c > a and a + c > b:
    print("As três retas formam um triângulo!")
    if a == b and a == c:
        print("esse triângulo, é um triângulo EQUILÁTERO")
    elif a == b and a != c or b == c and b != a or a == c != b:
        print("esse triângulo, é um triângulo ISÓSCELES")
    elif a != c and a != b:
        print("esse triângulo, é um triângulo ESCALENO")
else:
    print("Infelizmente não é possível formar um triângulo com os valores que você me ofereceu")
