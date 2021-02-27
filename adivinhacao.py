from os import system
import random

print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")
print("Informe um número entre 1 e 30")

numero_secreto = random.randint(1,30)
#system('cls')

tentativa = 1

while(tentativa <= 3):
    print(f"tentativas {tentativa} de 3")
    chute = int(input("Digite um numero: "))
    if (chute < 1 or chute > 30):
        print("Informe um número entre 1 e 30")
        continue
    tentativa += 1
    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    if (acertou):
        print("Voce acertou!")
        break
    else:
        if (maior):
            print("Voce errou! Seu chute foi maior que o número secreto")
        elif (menor):
            print("Voce errou! Seu chute foi menor que o número secreto")
print(f"O número Secreto foi {numero_secreto}")
print("Fim de Jogo.")
