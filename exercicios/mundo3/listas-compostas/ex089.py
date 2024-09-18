# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre o boletim contendo a média de cada um
# E permita que o usuário consegue mostrar as notas de cada aluno individualmente.

alunos = list()
aluno = list()

while True:
    nome = str(input("Nome do aluno: "))
    nota1 = int(input("Primeira nota: "))
    nota2 = int(input("Segunda nota: "))
    aluno.append(nome)
    aluno.append(nota1)
    aluno.append(nota2)
    alunos.append(aluno[:])
    aluno.clear()
    stop = str(input("Quer continuar [S/N]: ")).upper().strip()
    if stop == "N":
        break
for al in alunos:
    print(f"A média do aluno {al[0]} foi {(al[1] + al[2]) / 2}")

nota_individual = str(input("Gostaria de ver as notas dos alunos individualmente? [S/N]: ")).upper().strip()

if nota_individual == "S":
    print(40 * "=")
    print("NOTAS INDIVIDUAIS DOS ALUNOS")
    print(40 * "=")
    for al in alunos:
        print(f"As notas do aluno {al[0]} foram {al[1]} e {al[2]}")

print("\nPrograma finalizado!")