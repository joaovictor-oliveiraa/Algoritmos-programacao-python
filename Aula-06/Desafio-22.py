"""
Altere o programa de cálculo dos números primos, informando,
caso o número não seja primo, por quais número ele é divisível.
"""

while True:
    numero = int(input("Digite um número inteiro positivo: "))
    if numero > 0:
        break
    print("Por favor, digite um número maior que 0.")

if numero == 1:
    print(f"O número {numero} não é primo.")
else:
    quantidade_divisores = 0
    
    for i in range(1, numero + 1):
        if numero % i == 0:
            quantidade_divisores = quantidade_divisores + 1

    if quantidade_divisores == 2:
        print(f"O número {numero} é primo.")
    else:
        print(f"O número {numero} não é primo.")
        print("Ele é divisível pelos números: ", end="")
        
        for i in range(1, numero + 1):
            if numero % i == 0:
                print(i, end=" ")
        print()