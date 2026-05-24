"""
Um parque de diversões tem um brinquedo radical. Para entrar nele, a pessoa precisa:

Ter pelo menos 1.50m de altura (altura >= 1.50)
Ter 12 anos ou mais (idade >= 12)
Porém, se a pessoa estiver acompanhada dos pais, basta ter 1.30m de altura (independente da idade).
Escreva as perguntas usando input() e faça a árvore de decisão if/elif/else com and/or para liberar ou barrar a pessoa.
"""

altura = float(input("Digite sua altura em metros: "))
idade = int(input("Digite sua idade: "))
acompanhado = input("Você está acompanhado dos pais? (sim/nao): ").lower()

if (acompanhado == "sim" or acompanhado == "s") and (altura >= 1.30):
    print("Você pode entrar no brinquedo!")

elif (altura >= 1.50 and idade >= 12):
    print("Você pode entrar no brinquedo!")

else:
    print("Desculpe, você não pode entrar no brinquedo.")