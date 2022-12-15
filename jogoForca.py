import random


def jogar_foca():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    letras_acertadas = ["_", "_", "_", "_", "_", "_", "_", "_", "_", ]
    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):

        chute = input("Digite seu chute! ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
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

    if (acertou):
        print("Você acertou!")
    else:
        print("Você errou!")

    print("Fim de jogo!")


if (__name__ == "__main__"):
    jogar_foca()
