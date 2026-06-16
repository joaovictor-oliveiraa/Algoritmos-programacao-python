"""
Faça um programa que calcule o fatorial de um número inteiro
fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
"""

fat = 1

n1 = int(input("Digite um número para fatorar: "))

for N in range (n1, 0, -1):

    fat = fat * N

print(f"O fatorial de {n1}! é igual a {fat}")