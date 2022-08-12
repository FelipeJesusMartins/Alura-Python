from ctypes.wintypes import PLARGE_INTEGER
import forca
import advinhacao

print("*********************************")
print("********Escolha seu jogo*********")
print("*********************************")

jogo = int(input("(1) Forca\n(2) Advinhação\n"))

if(jogo == 1):
    print("Forca:")
    forca.Jogar()
elif(jogo == 2):
    print("Advinhação")
    advinhacao.Jogar()
else:
    print("Escolha um número válido")