"""Esta aba relaciona os dois jogos, com o usuário podendo
escolher entre os dois jogos e todas suas características
"""
#Importa os códigos dos jogos isoladamente, onde vão ser acionadas através das funções
import adivinhacao
import forca

def escolhe_jogo():

    # Chama a mensagem inicial
    print("***************")
    print("!!!Bem vindo!!!")
    print("***************")

    # Define qual o jogo do usuário
    chance = 0
    while (chance < 3):
        print("Escolha um dos jogos")
        print("(1) Jogo da Advinhação  (2) Jogo da Forca")
        jogo = int(input("Digite aqui o jogo: "))

        if (jogo == 1):  # Chama jogo da advinhação
            print("Jogando Advinhação")
            adivinhacao.jogar()
            break
        elif (jogo == 2):  # Chama jogo da forca
            print("Jogando Forca")
            forca.jogar()
            break
        else:  # Da mais 2 chances para o usuário digitar 1 ou 2
                print("Você deve digitar o número 1 ou 2")
                chance +=1
                continue

    if chance == 3:
        print("Você não foi capaz de escolher um jogo, reinicie e tente novamente")


if(__name__ == "__main__"):
    escolhe_jogo()