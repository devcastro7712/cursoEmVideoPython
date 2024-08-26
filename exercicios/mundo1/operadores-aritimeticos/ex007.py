# Escreva um programa que leia duas notas de um aluno e calcule a média entre elas.

while True:
    cadastroAluno = str(input("Deseja cadastrar um novo aluno? (sim) ou (não) ")).lower()
    if cadastroAluno == "sim" or cadastroAluno == "s":
        nomeDoAluno = str(input("Nome do aluno: "))
        nota1 = int(input("primeira nota: "))
        nota2 = int(input("Segunda nota: "))
        media = (nota1 + nota2) / 2
        print(f"O(a) aluno(a) {nomeDoAluno} teve a seguinte pontuação:\nNota do primeiro semestre: {nota1} pontos\n"
              f"Nota do segundo semestre: {nota2} pontos\n"
              f"Média anual: {media} pontos")
    else:
        print("Obrigado por usar o programa!")
        break