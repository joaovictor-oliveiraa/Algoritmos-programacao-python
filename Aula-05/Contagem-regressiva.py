"""
Crie um programa que faça uma contagem regressiva para estourar fogos.
Ele deve começar do 10 e ir até 1. Ao chegar no final, imprima 'BUM!!!'.
"""

print ("Inicio da primeira contagem")

for contagem in range(10,0,-1):
    print (f"{contagem}")
print("BUM!!!")


contador = 10
print("Inicio da segunda contagem")

while contador >= 1:
    print(f"{contador}")
    contador = contador - 1
print("BUM!!!")