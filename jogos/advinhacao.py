import random;

def Jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = round(random.randrange(1,101))
    total_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade ?")
    print("(1) Fácil\n(2) Médio\n(3) Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range (1,total_tentativas + 1):

        print("Tentativa {} de {}".format(rodada, total_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")

        if(chute_str is '' or chute_str is None):
            continue
        else:
            chute_int = int(chute_str)

        if (chute_int < 1 or chute_int > 100):
            print("Número fora do intervalo FDP")
            continue

        acertou = chute_int == numero_secreto
        maior = chute_int > numero_secreto
        menor = chute_int < numero_secreto

        if acertou:
            print("Você acertou e fez {} pontos !".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! seu chute foi maior que o número secreto")
            elif(menor):
                print("Você errou! seu chute foi menor que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute_int)
            pontos -= pontos_perdidos

        rodada = rodada + 1

    print("O número era: {}".format(numero_secreto))
    print("Fim do jogo!")

if(__name__ == "__main__"):
    Jogar()