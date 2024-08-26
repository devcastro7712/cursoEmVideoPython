# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime
anoAtual = datetime.date.today().year
anoDeNascimento = int(input("Qual seu ano de nascimento? "))
idade = anoAtual - anoDeNascimento


if idade < 18:
    divergenciaDeIdade = 18 - idade
    print(f"Você não pode se alistar, apenas daqui {divergenciaDeIdade} anos")
elif idade > 18:
    divergenciaDeIdade = idade - 18
    print(f"Você utrapassou o período de alistamento, deveria ter realizado a {divergenciaDeIdade} anos")
else:
    print("Você está no ano de alistamento!")