"""
Altere o programa anterior permitindo ao usuário informar as populações
e as taxas de crescimento iniciais. Valide a entrada e permita repetir
a operação.
"""

while True:
    pais_a = int(input("Digite a população inicial do país A: "))
    pais_b = int(input("Digite a população inicial do país B: "))

    if pais_a < pais_b:
        break
    print("A população do país A deve ser menos que o país B")

while True:
    taxa_a = float(input("Digite a taxa de crescimento do país A: "))
    taxa_b = float(input("Digite a taxa de crescimento do país B: "))

    if taxa_a > taxa_b:
        break
    print("A taxa de crescimento do país A deve ser maior que do país B")

taxa_a = (taxa_a / 100) + 1
taxa_b = (taxa_b / 100) + 1
ano = 0

while True:
    if pais_a >= pais_b:
        break

    ano = ano + 1
    pais_a = pais_a * taxa_a
    pais_b = pais_b * taxa_b

print(f"O país 'A' ultrapassará o país 'B' em {ano} anos")
print(f"População A: {round(pais_a, 2)} | População B: {round (pais_b, 2)}")