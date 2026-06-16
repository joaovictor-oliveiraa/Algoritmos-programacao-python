"""
Faça um programa que peça 10 números inteiros, calcule e mostre
a quantidade de números pares e a quantidade de números impares.
"""

pares = 0
impares = 0


for N in range(1, 11):
    numero = int(input(f"Digite o {N}º número: "))

    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")