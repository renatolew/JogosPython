#Tela inicial de seleção de jogos, exercício do curso introdutório de Python da Alura.

#Importando os jogos desenvolvidos.
import forca
import adivinhacao

def escolher_jogo():
    print("*********************************")
    print("****** Escolha o seu jogo! ******")
    print("*********************************")

    print("(1) Forca\n(2) Adivinhação")
    jogo = int(input("Qual jogo deseja jogar? "))

    if (jogo == 1):
        print("Jogando forca!\n\n")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando adivinhação!\n\n")
        adivinhacao.jogar()


#Garantindo que o código não seja executado automaticamente caso haja alguma interface prévia.
if(__name__ == "__main__"):
    escolher_jogo()
