from cgi import print_form
from site import check_enableusersite
import random

def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da forca!***")
    print("*********************************")

def Jogar():
    palavras = []
    with open("palavras.txt", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    palavra_secreta = palavras[random.randrange(0,len(palavras))].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not acertou and not enforcou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):

            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
        
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

        if(acertou):
            print("Você ganhou")
        else:
            print("Você errou")
            
        print("Fim do jogo")

if(__name__ == "__main__"):
    Jogar()