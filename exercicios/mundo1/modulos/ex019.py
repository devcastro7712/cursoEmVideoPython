# Um professor quer sortear um dos seus 4 alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles
# E escrevendo o nome do escolhido

import random

alunos = ["Lucas", "Gaby", "Loly", "Kenai"]
sortear = random.choice(alunos)

print(f"O aluno sorteado foi {sortear}")
