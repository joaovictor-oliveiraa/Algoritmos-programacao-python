"""
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer
número inteiro entre 1 a 10. O usuário deve informar de qual numero
ele deseja ver a tabuada.
"""

while True:
    numero = int(input("Digite um número de 1 a 10: "))

    if 1 <= numero <= 10:
        break
    
    print("O número deve ser entre 1 a 10")

print(f"Tabuada do {numero}:")

for N in range (1, 11):
    resultado = N * numero

    print(f"{numero} X {N} = {resultado}")