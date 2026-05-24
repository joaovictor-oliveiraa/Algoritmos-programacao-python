"""
Crie um código que pergunte um número inteiro ao usuário
e informe na tela se esse número é Positivo, Negativo ou Zero.
"""
numero = int(input("Insira um número: "))

if numero > 0:
    print(f"{numero} é um número positivo.")

elif numero == 0:
    print(f"{numero} é um número neutro.")

else:
    print(f"{numero} é um número negativo.")