"""
Você recebeu uma lista com as idades de um grupo de pessoas.
Calcule a média dessas idades (usando sum() e len()) e depois,
use um for para imprimir somente as idades que são MAIORES que a média.
"""

idades = [25, 45, 18, 30, 22, 60, 52]

soma = sum(idades)
total_pessoas = len(idades)
media = soma / total_pessoas

print(f"A média é {media}")

print(f"As idades maiores que 36 são:")

for idade in idades:
    
    if idade > 36:
        print(idade, end=" ")