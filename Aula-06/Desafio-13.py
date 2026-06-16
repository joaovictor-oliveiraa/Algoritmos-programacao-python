"""
Faça um programa que peça dois números, base e expoente,
calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem.
"""

base = int(input("Digite um número para base: "))
expoente = int(input("Digite um número para expoente: "))

contador = 0
resultado = 1

while contador < expoente:
    
    resultado = resultado * base
    contador = contador + 1

print(f"O número {base} elevado a {expoente} é {resultado}")