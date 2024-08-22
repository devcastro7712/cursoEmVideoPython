# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km
# e R$0,45 para viagens mais longas.

distanciaDaViagem = int(input("Quantos Km você percorrerá? "))
passagemAbaixoDe200Km = 0.50
passagemAcimaDe200Km = 0.45

if distanciaDaViagem <= 200:
    custoTotalDaViagem = distanciaDaViagem * passagemAbaixoDe200Km
    print(f"Você pagará R${custoTotalDaViagem} pela viagem")
else:
    custoTotalDaViagem = distanciaDaViagem * passagemAcimaDe200Km
    print(f"Você pagará R${custoTotalDaViagem} pela viagem")
