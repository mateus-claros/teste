import random


def Escolha(Comando, vida_A, forca_A, vida_B, Sair):
    if Comando == 1:
        vida_B -= forca_A
    elif Comando == 2:
        vida_A += forca_A
    elif Comando == 3:
        Sair = True

    return (vida_A, vida_B, Sair)


import random

Sair: bool = False

jogador_Vida = 100
jogador_Forca = 15

oponente_Vida = 100
oponente_Forca = random.randint(10, 30)

while (jogador_Vida > 0 and oponente_Vida > 0 and Sair != True):

    Comando = int(input("\nDigite o comando :"))

    Atualizar = Escolha(Comando, jogador_Vida, jogador_Forca, oponente_Vida, Sair)

    jogador_Vida = Atualizar[0]
    oponente_Vida = Atualizar[1]
    Sair = Atualizar[2]

    if (Comando == 1):
        print(f'\nVoce atacou dando {jogador_Forca} de dano no oponente.')
    elif (Comando == 2):
        print(f'\nVoce se curou em {jogador_Forca} de vida.')
    elif (Comando == 3):
        print(f'\nVoce saiu do Jogo.')

    if (Sair != True):
        escolha_oponente = random.randint(1, 2)

        Atualizar = Escolha(escolha_oponente, oponente_Vida, oponente_Forca, jogador_Vida, Sair)
        oponente_Vida = Atualizar[0]
        jogador_Vida = Atualizar[1]
        Sair = Atualizar[2]

        if (escolha_oponente == 1):
            print(f'\nOponente atacou dando {oponente_Forca} de dano no Jogador.')
        elif (escolha_oponente == 2):
            print(f'\nOponente se curou em {oponente_Forca} de vida.')

    print(f'\nSua vida atual :{jogador_Vida} \nVida do oponente {oponente_Vida}.')

if (jogador_Vida > 0 and oponente_Vida <= 0):
    print("Jogador Ganhou.")
elif (oponente_Vida > 0 and jogador_Vida <= 0):
    print("Oponente Ganhou.")
else:
    print("Empate")
