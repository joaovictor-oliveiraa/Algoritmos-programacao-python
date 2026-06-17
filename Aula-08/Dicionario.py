"""
Crie um dicionário com 3 nomes de produtos e seus respectivos preços
(ex: 'maçã': 3.50). Peça ao usuário para digitar o nome de um produto.
Se o produto existir no dicionário, imprima seu preço. Se não existir,
imprima 'Produto não encontrado'.
"""

tabela = {
    "arroz": 23.49,
    "feijão": 9.99,
    "leite": 5.50
}

nome_produto = input("Escolha um produto (Arroz, feijão ou leite): ").lower()

if nome_produto in tabela:
    print(f"O valor do {nome_produto} é de R$", tabela[nome_produto])

else:
    print(f"Produto {nome_produto} não encontrado")