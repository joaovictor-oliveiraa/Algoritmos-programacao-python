"""
Faça um programa que calcule o aumento de salário de um funcionário.

Para salários maiores que R$ 1500,00, aumento de 10%.
Para salários menores ou iguais a R$ 1500,00, aumento de 15%.
"""

salario = float(input("Qual seu salário atual? "))

if salario > 1500:
    print(f"Salário com aumento de 10% = {round (salario * 1.10, 2)}")

else:
    print(f"Salário com aumento de 15% = {round (salario *1.15, 2)}")