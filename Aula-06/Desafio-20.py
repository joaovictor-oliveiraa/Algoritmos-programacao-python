"""
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular
o fatorial várias vezes e limitando o fatorial a números inteiros positivos
e menores que 16.
"""

while True:
    while True:
        n1 = int(input("Digite um número entre 1 e 15: "))
        if 1 <= n1 < 16:
            break
        print("Erro! Número inválido.")
    
    print(f"{n1}! = ", end="")
    
    fat = 1
    for N in range(n1, 1, -1):
        fat = fat * N
        print(f"{N}", end=".")
        
    fat = fat * 1
    print(f"1 = {fat}")
    print("-" * 30)
    
    resposta = input("Calcular outro fatorial? (s/n): ").lower()
    if resposta != 's':
        print("Programa encerrado.")
        break