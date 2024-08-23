# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e consições de pagamento:
# À vista dinheiro/cheque: 10% de desconto.
# À vista cartão: 5% de desconto.
# Em até 2x no cartão: preço normal.
# em 3x ou mais no cartão: 20% de juros.

preco_do_produto = float(input("Preço do produto: R$"))
forma_de_pagamento = int(input("Escolha o número que corresponde a forma de pagamento escolhida:\n1- À vista dinheiro/cheque\n2- À vista cartão\n3- Em até 2x no cartão\n4- em 3x ou mais no cartão\n"))
desconto_avista = preco_do_produto - (preco_do_produto * 0.1)
desconto_avista_cartao = preco_do_produto - (preco_do_produto * 0.05)
preco_com_juros = preco_do_produto + (preco_do_produto * 0.2)

if forma_de_pagamento == 1:
    print(f"Você teve 10% de desconto e pagará R${desconto_avista:.2f}")
elif forma_de_pagamento == 2:
    print(f"Você teve 5% de desconto e pagará R${desconto_avista_cartao:.2f}")
elif forma_de_pagamento == 3:
    print(f"Não houve desconto, você pagará o valor integral de R${preco_do_produto}")
elif forma_de_pagamento == 4:
    print(f"Haverá uma taxa de juros de 20%, nesse caso você pagará R${preco_com_juros}")
else:
    print("Por favor selecione uma opção válida!")