"""
Faça um programa que leia 5 números e informe a soma e a média dos números.
"""

soma = 0
contador = 1

while contador <= 5:
    numero = float(input("Digite um número: "))

    soma = soma + numero
    media = soma / 5
    
    contador = contador + 1

print (f"A soma dos números é {soma}")
print(f"A média dos números é {media}")
