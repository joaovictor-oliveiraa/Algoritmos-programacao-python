"""
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo
"""

n = int(input("Quantos termos da série de Fibonacci você quer gerar? "))

termo1 = 1
termo2 = 1


print("Série de Fibonacci:")

if n >= 1:
    print(termo1, end=" ")
if n >= 2:
    print(termo2, end=" ")

for _ in range(3, n + 1):
    proximo_termo = termo1 + termo2
    print(proximo_termo, end=" ")
    
    termo1 = termo2
    termo2 = proximo_termo

print()