"""
Faça um programa que receba dois números inteiros
e gere os números inteiros que estão no intervalo compreendido por eles.
"""

i1 = int(input("Digite o primeiro número: "))
i2 = int(input("Digite o segundo número: "))

for N in range (i1, i2 + 1):
    print(f"{N}")