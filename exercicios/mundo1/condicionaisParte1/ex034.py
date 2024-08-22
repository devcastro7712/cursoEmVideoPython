# Escreva um programa que pergunte o salário de um funcinário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para salários inferiores ou iguais o aumento é de 15%.

salario = float(input("Qual o salário do funcionário?\nR$"))
aumentoSuperior = 0.1
aumentoInferior = 0.15

if salario > 1250:
    aumento = (salario * aumentoSuperior) + salario
    print(f"O salário do funcionário sofreu um reajuste de 10%, aumentando para R${aumento}")
else:
    aumento = (salario * aumentoInferior) + salario
    print(f"O salário do funcinário sofreu um reajuste de 15%, aumentando para R${aumento}")