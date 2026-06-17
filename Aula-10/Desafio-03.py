"""
Agora que temos o estoque.csv criado:

Abra o arquivo em modo de leitura ('r') e use o csv.reader para ler e imprimir
cada linha na tela com um laço for.
Depois, abra o mesmo arquivo em modo de adição/append ('a') e adicione
um novo produto usando writer.writerow(["Teclado", 80.0, 30]).
(Opcional) Abra o arquivo novamente e imprima para comprovar que o Teclado
foi adicionado no final!
"""

import csv

with open("estoque.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)

with open("estoque.csv", "a", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["Teclado", 80.0, 30])

print("\n--- Estoque Atualizado ---")
with open("estoque.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)