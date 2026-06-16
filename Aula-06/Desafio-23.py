"""
Faça um programa que mostre todos os primos entre 1 e N sendo N um número
inteiro fornecido pelo usuário. O programa deverá mostrar também o número
de divisões que ele executou para encontrar os números primos. Serão avaliados
o funcionamento, o estilo e o número de testes (divisões) executados.
"""

while True:
    n = int(input("Digite um número inteiro maior que 1: "))
    if n > 1:
        break
    print("Por favor, digite um número maior que 1.")

total_divisoes = 0

print(f"Números primos entre 1 e {n}:")

for numero in range(2, n + 1):
    eh_primo = True
    
    for i in range(2, numero):
        total_divisoes = total_divisoes + 1
        if numero % i == 0:
            eh_primo = False
            break
            
    if eh_primo:
        print(numero, end=" ")
print()
print(f"Total de divisões executadas: {total_divisoes}")