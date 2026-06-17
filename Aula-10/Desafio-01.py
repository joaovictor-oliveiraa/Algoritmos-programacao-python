"""
Crie um dicionário vazio agenda = {}. Peça ao usuário em um loop while o nome
e o telefone, e os guarde na agenda até ele digitar "sair".
No final, use json.dump para salvar a agenda em um arquivo agenda.json.
"""

import json

agenda = {}

while True:
    nome = input("Digite o nome (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":
        break
        
    telefone = input(f"Digite o telefone de {nome}: ")
    agenda[nome] = telefone

with open("agenda.json", "w", encoding="utf-8") as arquivo:
    json.dump(agenda, arquivo, ensure_ascii=False, indent=4)

print("Agenda salva com sucesso no arquivo 'agenda.json'!")