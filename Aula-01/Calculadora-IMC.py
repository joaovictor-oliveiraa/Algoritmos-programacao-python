"""
Descrição: Calculadora de IMC (Índice de Massa Corporal)
Autor: João Victor B. Oliveira
Data: 2026
"""

peso = float(input("Digite seu peso em Kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)

imc_ideal = 18.5 <= imc < 25

print(f"Seu IMC é: {round(imc, 2)}")

if (imc_ideal):
    print("Você está com o peso considerado ideal para sua altura.")
else:
    print("Você NÃO está com o peso considerado ideal para sua altura.")