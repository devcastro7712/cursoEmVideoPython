# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por km rodado

km_percorridos = float(input("Quantos km o carro percorreu? "))
valor_total_km = km_percorridos * 0.15
dias_aluguado = int(input("Por quantos dias o carro foi alugado? "))
valor_total_diarias = dias_aluguado * 60
custo_total = valor_total_km + valor_total_diarias

print(f"Valores a pagar referentes ao aluguel do veículo")
print(50*"=")
print(f"valor total referente aos dias percorridos: R${valor_total_diarias}\n"
      f"valor total referente aos quilometros rodados: R${valor_total_km}\n"
      f"valor total a ser pago pelo cliente: R${custo_total}")