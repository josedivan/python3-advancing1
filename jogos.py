import jogoDaAdivinhacao
import jogoForca

print('Escolha seu jogo!')
print('(1)JOGO DA FOCA', "(2)JOGO DA ADIVIANHAÇÃO")

jogo = int(input("Digite seu jogo: "))

if (jogo == 1):
    jogoForca.jogar_foca()

elif (jogo == 2):
    print("Bem-vindo ao jogo da Adivinhação")
    jogoDaAdivinhacao.jogar_adivinhacao()
