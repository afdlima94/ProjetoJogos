'''
Este é o jogo da forca, onde utiliza-se técnicas básicas de lógica de programação
e técnicas da linguagem Python para exportarmos palavras de arquivos de texto.
Esses arquivos são escolhidos a partir da escolha de categoria do usuário.
A partir disso é escolhida uma palavra aleatória do arquivo e definida como palavra secreta.
O usuário receberá quantas letras tem a palavra, e terá 7 chances para acertar.
Com laços for e while, além das técnicas if/else. Podemos imprir as letras que o usuário
acertou e informá-lo quantas chances ainda tem para acertar a palavra caso erre a letra.

Aproveite o jogo!!
'''


#Importa biblioteca random não qual utilizaremos para escolher um número aleatório
import random

def jogar(): #Função utilizada para chamar o jogo da forca

    # Chama a função que imprime mensagem de abertura
    mensagem_abertura()

    #O usuário escolhe a categoria das palavras
    print("Escolha uma das categorias")
    print("(1) Países")
    print("(2) Times de Futebol Brasileiros")
    print("(3) Animais")
    categoria = int(input("Digite um número de 1 a 3: "))


    #Define o valor da variável palavra_secreta, a partir do valor retornado pela função carrega_palavra_secreta()
    if (categoria == 1):
        nome_do_arquivo = "paises.txt"
        print("Você escolheu a categoria Países")
    elif (categoria == 2):
        nome_do_arquivo = "times_futebol_brasil.txt"
        print("Você escolheu a categoria Times de Futebol Brasileiros")
    else:
        nome_do_arquivo = "animais.txt"
        print("Você escolheu a categoria Animais")
    palavra_secreta = carrega_palavra_secreta(nome_do_arquivo)


    #Define o valor da variável letras_acertadas, a partir do valor retornado pela função inicializa_letras_acertadas()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    #Mostra para o usuário quantas letras tem a palavra secreta
    print(letras_acertadas)


    #Define as variáveis abaixo, quando as variáveisacertou e enforcou forem verdadeiras futuramente,
    # o jogo será encerrado.
    #Também vale para quando a variável errou tiver o valor 7
    acertou = False
    enforcou = False
    erros = 0


    #Laço que é repetido caso o usuário ainda não acertou ou esgotou as chances
    while (not acertou and not enforcou):

        # Define o valor da variável chute, a partir do valor retornado pela função pede_chute()
        chute = pede_chute()

        #Mostra as ações que serão feitas pelo programa, caso o usuário acerte uma letra da palavra secreta
        if(chute in palavra_secreta):
            #Chama a função marca_chute_correto, e insere a letra acertada no que é mostrado ao usuário
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)

        #Caso o usuário erre a letra, este será informado sobre quantas chances lhe restam
        else:
            erros += 1
            desenha_forca(erros)
            print("Você errou a letra")
            print('Você possui {} tentativas restantes'.format(7 - erros))


        #Define quando as variáveis do tipo bool recebem valor True e quebra o laço while
        enforcou = erros == 7
        acertou = '_' not in letras_acertadas

        #Mostra ao usuário as letras acertadas até então
        print(letras_acertadas)


    #Mostra as mensagem de campeão ou perdedor ao usuário quando o jogo termina
    if('_' not in letras_acertadas):
        mensagem_vencedor()
        print("A palavra era:")
        print(palavra_secreta)
    else:
        mensagem_perdedor()
        print("A palavra era:")
        print(palavra_secreta)
    print("Fim do jogo")

#Abaixo encontra-se as definições das funções utilizadas acima!

def mensagem_abertura(): #Função que imprime mensagem de abertura com algumas regras
    print("***************************")
    print("Bem vindo ao jogo da Forca!")
    print("***************************")

    print("\nNÃO EXISTEM PALAVRAS COMPOSTAS")
    print("OS ACENTOS ESTÃO OCULTOS")
    print("\nEx: constituiçao")

    print("\nVocê terá 7 tentativas, sendo que o acerto não conta como tentativa")

#Abaixo encontram-se as funções utilizadas acima

#Função onde carrega uma palavra para ser escolhida como a correta
def carrega_palavra_secreta(nome_do_arquivo):
    arquivo = open(nome_do_arquivo, "r") #Abre o arquivo e o lê
    palavras = [] #Monta uma lista vazia

    for linha in arquivo: #Para cada linha no arquivo texto é adicionado um valor na lista vazia
        linha = linha.strip() #Retira todos valores vazios da linha, deixando só a palavra
        palavras.append(linha)

    # Fecha o arquivo
    arquivo.close()

    # Escolhe um valor aleatório, variando de 0 até o valor correspondente ao tamanho da lista
    numero = random.randrange(0, len(palavras))
    # Define qual é a palavra secreta e deixa todas suas letras maiúsculas
    palavra_secreta = palavras[numero].upper()

    # Retorna a palavra secreta
    return palavra_secreta

#Função que retorna pro usúario uma lista mostrando quantas letras tem a palavra
def inicializa_letras_acertadas(palavra):
    return["_" for letra in palavra]

#Função que pede a letra de chute do usuário
def pede_chute():
    chute = input("Digite uma letra: ") #Recebe a letra
    chute = chute.strip().upper() #Transformar a letra em maiúscula e remove espaçõs em branco

    #Retorna a variável chute
    return chute

#Função que marca a letra acertada na lista mostrada ao usuário anteriormente
def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    # Faz um laço que confere se o chute esta presente na palavra_secreta, letra por letra
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

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

def mensagem_perdedor():
    print("Puxa, você foi enforcado!")
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

#Imprime o desenho da forca para cada erro do usuário
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
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

if(__name__ == "__main__"):
    jogar()