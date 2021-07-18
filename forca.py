# Jogo de forca, exercício do curso introdutório de Python da Alura.

import random

#Definindo a função de jogar forca que será chamada na interface inicial.
def jogar():

    mensagem_de_abertura()
    palavra_secreta = escolha_palavra_secreta()

    letras_acertadas = template_letras_acertadas(palavra_secreta)
    print("\n",letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    #laço para que o jogo continue e o loop se repita enquanto a forca não tiver sido feito e a palavra não tiver sido adivinhada.
    while(not enforcou and not acertou):

        chute = input_chute()

        #confirmando o acerto e inserindo a letra acertada na variável
        if(chute in palavra_secreta):
            chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)
            print("Esta letra não está na palavra, a corda está apertando! Você possui {} tentativas!".format(7-erros))

        #criando um limite de tentativas pro jogo, de forma que a variável enforcou de torne True caso o número de erros chegue a 6, interrompendo o loop.
        enforcou = erros == 7
        #definindo que a palavra estará completa e o jogo foi vencido quando não houverem mais caracteres vazios na palavra.
        acertou = "_" not in letras_acertadas
        print("\n",letras_acertadas)

    #Retornando mensagem de vitória ou derrota dependendo do resultado do jogo ao fim dos palpites.
    if(acertou):
        print("Parabéns, você ganhou!\n")
    else:
        print("Oh não! Você foi enforcado!")
        print("A palavra secreta era {}!\n".format(palavra_secreta))

    print("Fim do jogo!")




#Funções utilizadas no jogo:

def mensagem_de_abertura():
    print("*********************************")
    print("** Bem vindo ao jogo de forca! **")
    print("*********************************")

def escolha_palavra_secreta():
    #lendo um arquivo de texto para preparar as possíveis palavras secretas
    arquivo = open("palavras.txt", "r")
    palavras = []

    #criando uma lista de palavras com base no arquivo de texto
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    #fechando o arquivo de texto para não manter o canal aberto desnecessariamente.
    arquivo.close()

    #atribuindo um índice para cada palavra da lista.
    numero = random.randrange(0,len(palavras))

    #importando a palavra secreta aleatoriamente de um arquivo de texto.
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

#Criando palavra que representará as letras acertadas em caracteres 'vazios' de acordo com o numero de caracteres da palavra secreta.
def template_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def input_chute():
    chute = input("Qual letra a palavra contém? ")
    chute = chute.strip().upper()
    return chute

def chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1
    print("Bom palpite, esta letra está na palavra!!")

def desenha_forca(erros):
        print("  _______     ")
        print(" |/      |    ")

        if (erros == 1):
            print(" |      (_)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")

        if (erros == 2):
            print(" |      (_)   ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")

        if (erros == 3):
            print(" |      (_)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")

        if (erros == 4):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")

        if (erros == 5):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")

        if (erros == 6):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      /     ")

        if (erros == 7):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")

        print(" |            ")
        print("_|___         ")
        print()

#Garantindo que o jogo seja executado diretamente, caso requerido, e não dependa da interação com a interface inicial.
if(__name__ == "__main__"):
    jogar()