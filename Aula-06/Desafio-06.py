"""
Faça um programa que leia 5 números e informe o maior número.
"""

primeiro = float(input("Digite o 1º número: "))

maior_numero = primeiro
contador = 2

while contador <= 5:
    numero = float(input(f"Digite o {contador}º número: "))

    if numero > maior_numero:
        maior_numero = numero
    
    contador = contador + 1

print(f"O maior número digitado foi o {maior_numero}")