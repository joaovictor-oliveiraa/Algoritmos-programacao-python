"""
Peça os 3 lados de um triângulo. 
O programa deverá informar se os valores formam um triângulo. 
Caso formem, diga o tipo do triângulo:
"""

lado1 = float(input("Valor do primeiro lado do triângulo: "))
lado2 = float(input("Valor do segundo lado do triângulo: "))
lado3 = float(input("Valor do terceiro lado do triângulo: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 +lado3 > lado1):
    print("Seus valores podem formar um triângulo")
    
    if lado1 == lado2 == lado3:
        print("É um triângulo equilátero")
    elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
        print("É um triângulo isóceles")
    else:
        print("É um triângulo escaleno")

else:
    print("Seus valores não podem formar um triângulo")