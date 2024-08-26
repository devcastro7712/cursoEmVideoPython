# Desenvolva uma lógica que leia o peso e a altura de uma pessoa. Calcule seu IMC e mostre seu status, de acordo com a tabela abaixo.
# Abaixo de 18.5: Abaixo do peso.
# Entre 18.5 e 25: Peso ideal.
# Entre 25 a 30: Sobrepeso.
# Entre 30 até 40: Obesidade.
# Acima de 40: Obesidade Mórbida.
peso = float(input("Qual seu peso em quilos? "))
altura = float(input("Qual sua altura em metros? "))
imc = peso / (altura * altura)
pesoMinicoIdeal = altura * altura * 18.5
pesoMaximoIdeal = altura * altura * 25

if imc > 40:
    print(("Você tem Obesidade Mórbida!"))
    print((f"Seu peso ideal é entre {pesoMinicoIdeal:.2f}Kg e {pesoMaximoIdeal:.2f}Kg"))
elif imc >= 30:
    print("Você tem Obesidade!")
    print((f"Seu peso ideal é entre {pesoMinicoIdeal:.2f}Kg e {pesoMaximoIdeal:.2f}Kg"))

elif imc >= 25:
    print("Você está com Sobrepeso!")
    print((f"Seu peso ideal é entre {pesoMinicoIdeal:.2f}Kg e {pesoMaximoIdeal:.2f}Kg"))

elif imc >= 18.5:
    print(("Você está no peso ideal!"))
else:
    print("Você está abaixo do peso!")
    print((f"Seu peso ideal é entre {pesoMinicoIdeal:.2f}Kg e {pesoMaximoIdeal:.2f}Kg"))

