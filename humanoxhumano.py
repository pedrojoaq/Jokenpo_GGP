

pontosjogador1 = 0
pontosjogador2 = 0
empate= 0

while True:
    print("JOKENPO")

    jogador1 = int(input("JOGADOR 1, PEDRA/ 1 PAPEL/ 2 TESOURA/ 3 ?"))
    jogador2 = int(input("JOGADOR 2, PEDRA/ 1 PAPEL/ 2 TESOURA/ 3 ?"))

    if jogador1==jogador2:
        print("EMPATE!")
        empate = empate + 1
    elif (jogador1 == "1" and jogador2 == "3") or \
        (jogador1 == "3" and jogador2 == "2") or \
        (jogador1 == "2" and jogador2 == "1"):
        print("JOGADOR 1 GANHOU!")
        pontosjogador1 = pontosjogador1 + 1
    else:
        print("JOGADOR 2 GANHOU!")
        pontosjogador2 = pontosjogador2 + 1

    jogardenovo = int(input("jogar novamente ? sim ou nao : "))
    jogardenovo == "sim"
    
    sair = int(input("Deseja continuar ? Sair/ 1 ou Ficar/ 2 : "))
    if sair == "1":
        break

print(f"Jogador 1: {pontosjogador1}")
print(f"Jogador 2: {pontosjogador2}")
print(f"Empates:   {empate}")
print("MUITO OBRIGADO POR JOGAR! ") 






