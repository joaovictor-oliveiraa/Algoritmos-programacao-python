"""
Numa eleição existem três candidatos. Faça um programa que peça o número
total de eleitores. Peça para cada eleitor votar e ao final mostrar o número
de votos de cada candidato.
"""

while True:
    total_eleitores = int(input("Digite o número total de eleitores: "))
    if total_eleitores > 0:
        break
    print("Por favor, digite um número maior que 0.")

votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0

for i in range(1, total_eleitores + 1):
    while True:
        print(f"\nEleitor {i}, escolha seu candidato:")
        print("1 - Candidato 1")
        print("2 - Candidato 2")
        print("3 - Candidato 3")
        voto = int(input("Digite o número do seu voto: "))
        
        if voto == 1:
            votos_candidato1 = votos_candidato1 + 1
            break
        elif voto == 2:
            votos_candidato2 = votos_candidato2 + 1
            break
        elif voto == 3:
            votos_candidato3 = votos_candidato3 + 1
            break
        else:
            print("Voto inválido! Escolha entre 1, 2 ou 3.")


print("RESULTADO DA ELEIÇÃO:")
print(f"Candidato 1: {votos_candidato1} voto(s)")
print(f"Candidato 2: {votos_candidato2} voto(s)")
print(f"Candidato 3: {votos_candidato3} voto(s)")