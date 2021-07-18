# Jogo de adivinhação, exercício do curso introdutório de Python da Alura.

#importando a função random para randomização do número a ser adivinhado.
import random

#Definindo a função de jogar adivinhação que será chamada na interface inicial.
def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    #Definindo o número secreto a ser adivinhado e criando variáveis de pontos e total de tentativas a serem utilizadas posteriormente..
    numero_secreto = random.randrange(1,101) #cria um número inteiro entre 1 e 100 (segundo parametro é excludente)
    total_de_tentativas = 0
    pontos = 1000

    #selecionando o nível de dificuldade do jogo, que por sua vez irá definir o número total de tentativas de acerto.
    print("Qual o nível de dificuldade desejado?")
    print("(1) Fácil\n(2) Médio\n(3) Difícil")
    dificuldade = int(input("\nEscolha seu nível: "))

    if (dificuldade == 1):
        total_de_tentativas = 12
    elif (dificuldade == 2):
        total_de_tentativas = 8
    elif (dificuldade == 3):
        total_de_tentativas = 5

    #Criando o laço que permite que o jogo se repita enquanto as três tentativas não sejam esgotadas.
    for tentativa_atual in range(1,total_de_tentativas + 1):
        #Informando o usuário o número de tentativas restantes.
        print("\nTentativa {} de {}".format(tentativa_atual, total_de_tentativas))
        #Pedindo input do usuário na tentativa de adivinhar o número.
        chute_str = input("Digite um número entre 1 e 100: ")

        #Transformando o input, que por padrão é uma string, em um número inteiro para a comparação futura com o numero secreto.
        chute = int(chute_str)
        if(chute < 1 or chute > 100):
                print("Você deve digitar um número entre 1 e 100: ")
                continue

        #Confirmando ao usuário seu número digitado.
        print("Você digitou ", chute)

        #Criando pequenas funções relativas à comparação do input com o número secreto para deixar o código seguinte mais legível.
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        #Condicionais de comparação entre o input e o número secreto.
        if (acertou):
            print("Parabéns, você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(menor):
                print("Você errou! Seu número é menor do que o número secreto.")
            elif(maior):
                print("Você errou! Seu número é maior do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute) #número absoluto da diferença entre numero secreto e chute.
            pontos = pontos - pontos_perdidos #subtraindo os pontos relativos ao erro.


    print("Fim do jogo!")


#Garantindo que o jogo seja executado diretamente, caso requerido, e não dependa da interação com a interface inicial.
if(__name__ == "__main__"):
    jogar()