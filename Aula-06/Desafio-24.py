"""
Faça um programa que calcule e mostre a média aritmética de N notas.
"""

while True:
    n = int(input("Quantas notas você deseja digitar? "))
    if n > 0:
        break
    print("Por favor, digite um número maior que 0.")

soma_notas = 0

for i in range(1, n + 1):
    while True:
        nota = float(input(f"Digite a {i}ª nota: "))
        if 0 <= nota <= 10:
            break
        print("Nota inválida! A nota deve ser entre 0 e 10.")
        
    soma_notas = soma_notas + nota

media = soma_notas / n

print(f"A média aritmética das {n} notas é: {media:.2f}")