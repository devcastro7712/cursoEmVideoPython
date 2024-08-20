# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario_atual = float(input("Determine o salário do funcionário: R$"))
novo_salario = salario_atual + (salario_atual * 15 / 100)

print(f"O funcionário recebe R${salario_atual}, e com o reajuste passará a receber R${novo_salario}")