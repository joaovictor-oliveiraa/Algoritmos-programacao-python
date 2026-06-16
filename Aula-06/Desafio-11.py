"""
Altere o programa anterior para mostrar no final a soma dos números.
"""

i1 = int(input("Digite o primeiro número: "))
i2 = int(input("Digite o segundo número: "))

soma = 0

for N in range (i1, i2 + 1):
    
    soma = soma + N
    print(f"{N}")

print(f"A soma de todos os inteiros dentro do intervalo entre os número é: {soma}")
