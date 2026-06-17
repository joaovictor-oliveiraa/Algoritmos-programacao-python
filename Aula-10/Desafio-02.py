"""
Foi te pedida a criação de um sisteminha básico de controle de estoque.
Crie uma lista de listas chamada produtos, por exemplo:
[["Notebook", 3500.0, 5], ["Mouse", 120.0, 15]]. Abra um arquivo chamado
estoque.csv em modo de escrita ('w') e use o módulo csv.writer para escrever
o cabeçalho ["Produto", "Preco", "Quantidade"] e logo após,
as linhas dos produtos. Ao final, confira se o arquivo foi criado com as
vírgulas corretamente.
"""

import csv

produtos = [
    ["Notebook", 3500.0, 5],
    ["Mouse", 120.0, 15],
    ["Teclado Mecânico", 250.0, 10],
    ["Monitor 24'", 950.0, 7]
]

with open("estoque.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    
    escritor.writerow(["Produto", "Preco", "Quantidade"])
    escritor.writerows(produtos)

print("Arquivo 'estoque.csv' criado com sucesso!")