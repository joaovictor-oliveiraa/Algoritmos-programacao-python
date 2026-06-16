"""
Faça um programa que leia 1 número inteiro e imprima
o seu sucessor e o seu antecessor.
"""

while True:
    print("Para sair digite 0 ")
    numero = int(input("Digite um número: "))

    if numero == 0:
        print("Saindo do programa")
        break
    
    sucessor = numero + 1
    antecessor = numero - 1

    print(f"O sucessor é {sucessor}")
    print(f"O antecessor é {antecessor}")