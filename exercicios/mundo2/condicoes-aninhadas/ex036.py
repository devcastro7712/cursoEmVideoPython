# Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor mensal sabendo que ele não pode ultrapassar 30% do salário ou então o emprestimo será negado.

print("Lucas Imóveis")
print(50 * "=-")

valorDaCasa = float(input("\nQual o valor da casa? "))
salarioComprador = float(input("\nQual seu salário mensal? "))
anosAPagar = int(input("\nEm quantos anos você pretende comprar o imóvel? (até 35 anos)"))


conversaoEmMeses = anosAPagar * 12
prestacao = valorDaCasa / conversaoEmMeses
valorMaximoFinanciavelPorSalario = salarioComprador * 30 / 100


if anosAPagar <= 35:
    if valorMaximoFinanciavelPorSalario > prestacao:
        print("\nParabéns, seu financiamento foi concluido com sucesso!")
        informacoes = str(input("Caso queira ver as informações do seu financiamento, digite SIM, caso não queira, digite qualquer outra tecla!")).lower().strip()
        if informacoes == "sim":
            print(f"\nvalor do financiamento: R${valorDaCasa:.2f}\n"
                  f"número total de parcelas: {conversaoEmMeses}\n"
                  f"valor da prestação: R$ {prestacao:.2f}")
        else:
            print("\nTudo bem, qualquer dúvida pode me contatar!")
    else:
        print("\ninfelizmente não é possível realizar seu financiamento,\ntente aumentar o número de anos a pagar ou procure um imóvel com um valor mais acessível")
else:
    print("\nSó é possível financiar em até 35 anos, refaça a simulação!")