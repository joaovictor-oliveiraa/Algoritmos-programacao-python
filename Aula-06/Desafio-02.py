"""
Faça um programa que peça para o usuário digitar uma nota entre 0 e 10.
Sempre que o usuário digitar um valor inválido (menor que 0 ou maior que 10),
o programa deve imprimir "Nota Inválida" e pedir para ele digitar a nota novamente.
Só deve aceitar e encerrar o programa quando a nota for válida.
"""

while True:
    nota = float(input("Digite uma nota de 0 a 10: "))
    if 0 <= nota <= 10:
        print(f"Nota {nota} registrada")
        break

    else:
        print("Nota inválida")