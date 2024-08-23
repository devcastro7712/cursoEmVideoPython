# A conferência nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a sua idade.
# Até 9 anos: MIRIN
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER

import datetime

anoAtual = datetime.date.today().year
anoDeNascimento = int(input("Qual seu ano de nascimento: "))
idade = anoAtual - anoDeNascimento
print(f"Você tem {idade} anos")

if idade <= 9:
    print("MIRIN")
elif idade <= 14:
    print("INFANTIL")
elif idade <= 19:
    print("JÚNIOR")
elif idade <= 20:
    print("SÊNIOR")
else:
    print("MASTER")

