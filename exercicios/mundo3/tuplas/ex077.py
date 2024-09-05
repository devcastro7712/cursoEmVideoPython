# Crie um programa que tenha uma tupla com várias palavras (não use acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ("casa", "carro", "mesa", "python")

for palavra in palavras:
    print(f"\nNa palavra {palavra} temos: ", end= "")
    for letra in palavra:
        if letra.lower() in "aeiou":
            print(letra, end= " ")
