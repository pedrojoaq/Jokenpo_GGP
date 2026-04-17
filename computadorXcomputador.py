import random
rodada = int(input("COMEÇAR: 1 / SAIR: 2 "))

pedra = 1
papel = 2
tesoura = 3
contador1 = 0
contador2 = 0

while rodada != 2:
    computador1 = random.randint(1,3)
    computador2 = random.randint(1,3)

    print("COMPUTADOR 1: ", computador1, "COMPUTADOR 2: ", computador2)

    if computador1 == 1:
        if computador2 == 1:
            print("EMPATE")
        elif computador2 == 2:
            print("PAPEL GANHOU")
            contador2 += 1
        else:
            print("PEDRA GANHOU")
            contador1 += 1
    elif computador1 == 2:
        if computador2 == 1:
            print("PAPEL GANHOU")
            contador1 += 1
        elif computador2 == 2:
            print("EMPATE")
        else:
            print("TESOURA GANHOU")
            contador2 += 1
    elif computador1 == 3:
        if computador2 == 1:
            print("PEDRA GANHOU")
            contador2 += 1
        elif computador2 == 2:
            print("TESOURA GANHOU")
            contador1 += 1
        else:
            print("EMPATE")
    rodada = int(input("CONTINUAR: 1 / SAIR: 2 "))

print("PLACAR GERAL:")
print("COMPUTADOR 1: ", contador1)
print("COMPUTADOR 2: ", contador2)