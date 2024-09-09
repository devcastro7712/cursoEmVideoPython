# Crie um programa que vai ler vários números e colocar em uma lista, depois disso, mostre:
# Quantos números foram digitados,
# A lista de valores, ordenada de forma decrescente.
# Se o valor 5 foi digitado e está ou não na lista.

lista = []
init = str(input("Deseja adicionar um valor a lista [S/N]: ")).upper().strip()[0]
while True:
    while init == "S":
        valor = int(input("Adicione um valor a lista: "))
        lista.append(valor)
        init = str(input("Deseja adicionar um valor a lista [S/N]: ")).upper().strip()[0]
    print("\n")
    print(70*"=")
    print("leitura finalizada!".upper().center(70))
    print(70 * "=")
    print(f"\n- Foram digitados {len(lista)} valores a lista!")
    lista.sort(reverse=True)
    print(f"- A lista ordenada de forma decrescente: {lista}")
    if 5 in lista:
        print("- O valor 5 está na lista!")
    else:
        print("- O valor 5 não está na lista!")

    break