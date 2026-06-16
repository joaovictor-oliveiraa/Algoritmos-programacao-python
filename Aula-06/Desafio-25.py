"""
Faça um programa que peça para n pessoas a sua idade, ao final o programa
devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60
e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa,
conforme a média calculada.
"""

while True:
    n = int(input("Quantas pessoas tem na turma? "))
    if n > 0:
        break
    print("Por favor, digite um número maior que 0.")

soma_idades = 0

for i in range(1, n + 1):
    while True:
        idade = int(input(f"Digite a idade da {i}ª pessoa: "))
        if idade >= 0:
            break
        print("Idade inválida! Digite uma idade maior ou igual a 0.")
        
    soma_idades = soma_idades + idade

media = soma_idades / n

print("-" * 30)
print(f"Média de idade da turma: {media:.1f} anos")

if 0 <= media <= 25:
    print("A turma é: JOVEM")
elif 26 <= media <= 60:
    print("A turma é: ADULTA")
else:
    print("A turma é: IDOSA")