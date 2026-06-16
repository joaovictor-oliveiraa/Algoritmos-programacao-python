"""
Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e quantidade de alunos para cada turma.
As turmas não podem ter mais de 40 alunos.
"""

while True:
    quantidade_turmas = int(input("Digite a quantidade de turmas: "))
    if quantidade_turmas > 0:
        break
    print("Por favor, digite uma quantidade de turmas maior que 0.")

total_alunos = 0

for i in range(1, quantidade_turmas + 1):
    while True:
        alunos_turma = int(input(f"Digite a quantidade de alunos da {i}ª turma: "))
        if 0 <= alunos_turma <= 40:
            break
        print("Quantidade inválida! As turmas não podem ter mais de 40 alunos.")
        
    total_alunos = total_alunos + alunos_turma

media = total_alunos / quantidade_turmas

print(f"Média de alunos por turma: {media:.1f} alunos")