"""
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
"""

N = int(input("Quantos números você deseja digitar? "))

while True:
    primeiro = float(input("Digite o 1º número (entre 0 e 1000): "))
    if 0 <= primeiro <= 1000:
        break
    print("Erro! O número deve estar entre 0 e 1000.")


maior = primeiro
menor = primeiro
soma = primeiro


for i in range(2, N + 1):
    
    
    while True:
        numero = float(input(f"Digite o {i}º número (entre 0 e 1000): "))
        if 0 <= numero <= 1000:
            break
        print("Erro! O número deve estar entre 0 e 1000.")
    
    soma += numero
    
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Soma dos valores: {soma}")