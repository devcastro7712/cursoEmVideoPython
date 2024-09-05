# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mestre:
# Apenas os 5 primeiros colocados.
# Os últimos 4 colocados da tabela.
# Uma lista com os times em ordem alfabética.
# Em que posição da tabela está o time do São Paulo.

tabela = ("botafogo", "fortaleza", "palmeiras", "flamengo", "cruzeiro", "sao paulo", "bahia", "vasco", "atletico mineiro", "internacional",
          "bragantino", "athletico paranaense", "criciuma", "juventude", "gremio", "fluminense", "corinthians", "vitória", "cuiabá", "atletico goianiense")

while True:
    menu = int(input(
        "O que deseja consultar?\n[1] Os 5 primeiros colocados\n[2] Os últimos 4 colocados da tabela\n[3] A ordem alfabética dos times do campeonato"
        "\n[4] A posição de um time na tabela\nEscolha: "))

    if menu == 1:
        print(f"\nOs 5 primeiros colocados são:\n{tabela[0:5]}")
        break
    elif menu == 2:
        print(f"\nOs 4 últimos colocados são:\n{tabela[-4:]}")
        break
    elif menu == 3:
        print(f"\nA ordem alfabética dos times é a seguinte:\n{sorted(tabela)}")
        break
    elif menu == 4:
        while True:
            escolha = str(input("Qual time você deseja encontrar a posição: "))
            if escolha.lower() in tabela:
                print(f"A posição do time {escolha.capitalize()} é {tabela.index(escolha.lower()) + 1}° colocado")
                break
            else:
                retry: str = input("O time não está na tabela. Deseja tentar novamente? (s/n): ").strip().lower()
                if retry == 'n':
                    break
        if retry == 'n':
            continue
        break
    else:
        print("\n\nOpção incorreta, tente novamente!")