# Escreva um programa que converta a temperatura digitada em Celsius e converta para fahrenheit.

temperatura_C = float(input("Qual a temperatura em °C? "))
temperatura_F = (temperatura_C * 9 / 5) + 32
print(f"{temperatura_C}°C equivalem a {temperatura_F}°F")