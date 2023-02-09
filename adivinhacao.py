"""Este é o jogo da advinhação, nele o usuário escolhe um nível de dificuldade,
após isso o programa sorteia um número aleatório entre 1 e 100. Após isso o usuário
deve através de tentativas e dicas acertar o número aleatório gerado.
A cada erro o usuário recebe uma dica, se o número do seu chute é maior ou menor
que o número gerado aleatóriamente.
Após todas as tentativas (as quais estão relacionadas com o nível selecionado), o jogador
perde a partida. Se acertar antes de se esgotarem as tentativas, ele vence"""

import random

def jogar():

    #Chama a função que imprime a mensagem inicial
    mensagem_inicial()

    #Chama a função que sorteia um número e o guarda dentro da variável numero_secreto
    numero_secreto = sorteia_numero()

    #Define a pontuação inicial
    pontos = 1000

    #Escolhe o nível de dificuldade
    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    #Chama a função que define o total de tentativas e guarda dentro da variavel
    total_de_tentativas = tentativas()

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        #Chama a função que confere se o chute está entre 1 e 100, e guarda o valor na variável chute
        chute = chute_certo()

        # Verifica se o número escolhido está entre 1 e 100
        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        #Chama a mensagem para o vencedor
        if(acertou):
            mensagem_vencedor()
            print("Você fez {} pontos!".format(pontos))
            break
        #Mostra que o usuário errou e da uma dica ao mesmo
        else:
            if (maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")

        #Calcula a pontuação do usuário
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

        #Imprime na tela a mensagem para o perdedor
        if(rodada == total_de_tentativas):
            mensagem_perdedor()
            print("O número secreto era {}, e você fez {} pontos".format(numero_secreto, pontos))

    print("Fim do jogo")

#Abaixo se encontra as definições das funções utilizadas acima

#Exibe na tela a mensagem inicial do jogo
def mensagem_inicial():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

#Sorteia um número entre 1 e 100
def sorteia_numero():
    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    return numero_secreto

# Define o total de tentivas que o usuário vai ter
def tentativas():

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5
    return total_de_tentativas

#Recebe um valor para o chute e o guarda dentro da variável chute
def chute_certo():

    #Recebe o valor do chute e o transforma em inteiro
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou " , chute_str)
    chute = int(chute_str)

    return chute

#Imprime a mensagem para o vencedor e quantos pontos ele fez
def mensagem_vencedor():

    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


#Imprime a mensagem para o perdedor e quantos pontos ele fez
def mensagem_perdedor():

    print("Puxa, suas chances acabaram!")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

if(__name__ == "__main__"):
    jogar()