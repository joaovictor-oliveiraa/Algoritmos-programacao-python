"""
Crie uma função chamada verifica_maioridade que recebe uma idade.
A função não deve ter print. Ela deve retornar a string "Maior de Idade"
ou "Menor de Idade".
"""

def verifica_maioridade(idade):
    if idade >= 18:
        return "Maior de Idade"
    else:
        return "Menor de Idade"