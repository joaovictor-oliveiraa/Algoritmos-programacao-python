"""
Faça um programa que, dado um conjunto de N números,
determine o menor valor, o maior valor e a soma dos valores.
"""

N = int(input("Escolha quantos números você deseja digitar: "))

primeiro = float(input("Digite o 1º número: "))


maior = primeiro
menor = primeiro
soma = primeiro


for i in range(2, N + 1):
    numero = float(input(f"Digite o {i}º número: "))
    
    soma += numero
    
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Soma dos valores: {soma}")