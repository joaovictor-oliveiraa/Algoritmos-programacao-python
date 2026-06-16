"""
Faça um programa que peça um número inteiro e determine
se ele é ou não um número primo. Um número primo é aquele
que é divisível somente por ele mesmo e por 1.
"""

while True:
    numero = int(input("Digite um número inteiro positivo: "))
    if numero > 0:
        break
    print("Por favor, digite um número maior que 0.")

if numero == 1:
    print(f"O número {numero} não é primo.")
else:
    eh_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            eh_primo = False
            break

    if eh_primo:
        print(f"O número {numero} é primo.")
    else:
        print(f"O número {numero} não é primo.")