"""
Crie uma função chamada eh_par que receba um número como parâmetro e
retorne True se for par, e False se for ímpar. Em seguida, peça um número
ao usuário, chame a função, e imprima se o número é Par ou Ímpar baseado
no retorno dela.
"""

def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

num_usuario = int(input("Digite um número inteiro: "))

if eh_par(num_usuario):
    print("O número é Par")
else:
    print("O número é Ímpar")