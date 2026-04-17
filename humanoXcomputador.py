infinito = 1
placarHumano = 0
placarMaquina = 0

print("Jokenpo!")
print("Escolha a modalidade: ")
print("H x H - 1")
print("H x M - 2")
print("M x M - 3")
escolhaModalidade = int(input("Escolha modalidade: "))

if(escolhaModalidade == 1):
    print("Nada ainda...")
elif(escolhaModalidade == 2):
    print("Nada ainda...")
elif(escolhaModalidade == 3):
    while infinito != 0:
        print("Pedra - 1")
        print("Papel - 2")
        print("Tesoura - 3")
        escolha = int(input("Digite sua escolha: "))

        while escolha < 1 or escolha > 3:
            print("Escolha um numero entre 1 e 3!")
            escolha = int(input("Digite sua escolha: "))

        import random
        numeroAleatorio = random.randint(1, 3)

        print(f"Maquina escolheu: {numeroAleatorio}")

        if(escolha == numeroAleatorio):
            print("Empate!")

        elif(escolha == 1):
            if(numeroAleatorio == 2):
                print("Maquina venceu!")
                placarMaquina+= 1
            elif(numeroAleatorio == 3):
                print("Humano venceu!")
                placarHumano+= 1

        elif(escolha == 2):
            if(numeroAleatorio == 1):
                print("Humano venceu!")
                placarHumano+= 1
            elif(numeroAleatorio == 3):
                print("Maquina venceu!")
                placarMaquina+= 1

        elif(escolha == 3):
            if(numeroAleatorio == 1):
                print("Maquina venceu!")
                placarMaquina+= 1
            elif(numeroAleatorio == 2):
                print("Humano venceu!")
                placarHumano+= 1
        
        print("Continuar - 1")
        print("Sair - 0")
        escolhaContinuar = int(input("Escolha: "))
        
        if(escolhaContinuar == 0):
            print("Placar")
            print(f"H - {placarHumano} X M - {placarMaquina}")
            infinito = 0

