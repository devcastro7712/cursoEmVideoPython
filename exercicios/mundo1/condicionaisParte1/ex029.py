# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada km acima do limite.

velocidadeDoCarro = int(input("Qual a velocidade que o carro estava: "))
multa = 7.00

if velocidadeDoCarro > 80:
    velocidadeUltrapassada = velocidadeDoCarro - 80
    valorDaMulta = velocidadeUltrapassada * 7
    print(f"Você foi multado em R${valorDaMulta} por ultrapassar {velocidadeUltrapassada}km/h da velocidade máxima permitida de 80Km/h")
else:
    print("Você estava dentro da velocidade permitida, continue respeitando as leis de trânsito!")