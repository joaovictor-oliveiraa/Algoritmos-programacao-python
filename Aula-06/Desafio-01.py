"""
Peça um número N ao usuário. Use um loop for ou while para
calcular e exibir a SOMA de todos os números PARES entre 1 e N.
"""

soma = 0
n = int(input("Digite o valor final N: "))

for n in range (0, n + 1, 2):
    print(f"{n}")
    soma = soma + n

print(f"Soma de todos os números PARES {soma}")