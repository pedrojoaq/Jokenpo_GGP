import random
import time
infinito = 1
placarHumano = 0
placarMaquina = 0

maoTres = '''
                          ++####                        
                          ++    ##                      
              ########    ++      ##                    
            ##      ##    ++      ##                    
            ##        ##  ++      ##  ####--            
            ##        ##  ++      ######  MM            
            ##        ##  ++      ####      ##          
            ##        ####++      ####      ##          
              ##        ##++      ##        MM            
              ##        ##++      ##       MM            
              ##        ##++    ####       MM            
                ##              ##         MM##          
                ##                         --####        
                ++++++++++++++         ++++    ##        
                ##            ##       ##      ##        
              ##              ##       ##      ##        
            ##                ##       ##      ##        
            ##              ##         ##    ##          
            ##        ######           ##    ##          
            ##              ##           ####            
              ##              ##          MM            
                ##            ##          --            
                  ##          ##        ##--            
                    ####  ++##        ####              
                        ################                
'''

maoDois = '''
                             ####                        
                          ##     ##                      
              ########    ##       ##                    
            ++      ##    ##       ##                    
            ++      ##    ##       ##                    
            ++        ##  ##       ##                    
            ++         ##  ##      ##                    
            ++          ######     ##                    
              ##        ####      ##                    
              ##        ####      ##                    
                ##            ####  ++++######          
                ##            ##      ++    ####        
                ##    ########        ++##    ##        
                  ####      ##        ##      ##        
                ##            ##      ##      ##        
              ::              ##      ##      ##        
              ++             ##       ##      ##          
              ++        ######  ##    ####    ##          
              ++              ##  ####    ####            
              ##              ##          ##            
              ##              ##          ##            
                  ##          ##        ##              
                    ####    ##        ####              
                        ################                
'''

maoUm = '''
                  ######                                
                ##      ##                              
                ##      ##                              
                ##      ##                              
                ##        ##                            
                ##        ##                            
                ##        ##                            
                ##        ##                            
                  ##      ####                          
                  ##      ##  ##  ######                
                  ##      ##    ##      ##::##          
                  ##      ##    ##      ##mm####        
                  ####      ####        ##      ##        
                ##            ##        ##      ##        
              ##              ##        ##      ##        
              ##              ##        ##      ##        
              ##              ##        ##    ##          
              ##        ######  ##    ####    ##          
              ##              ##  ####    ####            
              ##              ##          MM            
                ##            ##          mm            
                  ##          ##        ##mm            
                    ####    ##        ####              
                        ################                
'''

jokenpo = '''
       __   ____     __ __    ______    _   __    ____    ____
      / /  / __ |   / //_/   / ____/   / | / /   / __ |  / __ |
 __  / /  / / / /  / ,<     / __/     /  |/ /   / /_/ / / / / /
/ /_/ /  / /_/ /  / /| |   / /___    / /|  /   / ____/ / /_/ /
|____/   |____/  /_/ |_|  /_____/   /_/ |_/   /_/      |____/
'''

divisao = '''
===============================================================
'''

ja = '''
       __    ___     __
      / /   /   |   / /
 __  / /   / /| |  / /
/ /_/ /   / ___ | /_/
|____/   /_/  |_|(_)
'''

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

vs = '''
 _    __   _____
| |  / /  / ___/
| | / /   |__  |
| |/ /   ___/ /
|___/   /____/
'''

print(jokenpo)
print(divisao)
print("MODALIDADES")
print(" ")
print("Jogador VS Jogador - 1")
print(" ")
print("Jogador VS Computador - 2")
print(" ")
print("Computador VS Computador - 3")
print(" ")
escolhaModalidade = int(input("Escolha a modalidade: "))

while escolhaModalidade < 1 or escolhaModalidade > 3:
        print(" ")
        print("Escolha um número entre 1 e 3!")
        print(" ")
        escolha = int(input("Digite novamente sua escolha: "))

if(escolhaModalidade == 1):
    print("Nada ainda...")

elif(escolhaModalidade == 2):
    while infinito != 0:
        print(divisao)
        print("ESCOLHA SUA JOGADA")
        print(" ")
        print("Pedra - 1")
        print(" ")
        print("Papel - 2")
        print(" ")
        print("Tesoura - 3")
        print(" ")
        escolha = int(input("Digite sua escolha: "))

        while escolha < 1 or escolha > 3:
            print(" ")
            print("Escolha um numero entre 1 e 3!")
            print(" ")
            escolha = int(input("Digite novamente sua escolha: "))

        numeroAleatorio = random.randint(1, 3)

        print(" ")
        print(divisao)
        time.sleep(1)
        print(" ")
        print(maoTres)
        time.sleep(1)
        print(" ")
        print(maoDois)
        time.sleep(1)
        print(" ")
        print(maoUm)
        time.sleep(1)
        print(" ")
        print(ja)
        time.sleep(1)
        print(" ")
        print(divisao)

        if(escolha == numeroAleatorio):
            print("Empate!")

        elif(escolha == 1):
            print("SUA ESCOLHA:")
            time.sleep(1)
            print(pedra)
            print(" ")
            time.sleep(1)
            print(vs)
            time.sleep(1)
            print(" ")
            print("ESCOLHA DO COMPUTADOR:")
            time.sleep(1)
            if(numeroAleatorio == 2):
                print(papel)
                print(" ")
                time.sleep(2)
                print(divisao)
                print("COMPUTADOR venceu!")
                placarMaquina+= 1
            elif(numeroAleatorio == 3):
                print(tesoura)
                print(" ")
                time.sleep(2)
                print(divisao)
                print("HUMANO venceu!")
                placarHumano+= 1

        elif(escolha == 2):
            print("SUA ESCOLHA:")
            time.sleep(1)
            print(papel)
            print(" ")
            time.sleep(1)
            print(vs)
            time.sleep(1)
            print(" ")
            print("ESCOLHA DO COMPUTADOR:")
            time.sleep(1)
            if(numeroAleatorio == 1):
                print(pedra)
                print(" ")
                time.sleep(2)
                print(divisao)
                print("HUMANO venceu!")
                placarHumano+= 1
            elif(numeroAleatorio == 3):
                print(tesoura)
                print(" ")
                time.sleep(2)
                print(divisao)
                print("COMPUTADOR venceu!")
                placarMaquina+= 1

        elif(escolha == 3):
            print("SUA ESCOLHA:")
            time.sleep(1)
            print(tesoura)
            print(" ")
            time.sleep(1)
            print(vs)
            time.sleep(1)
            print(" ")
            print("ESCOLHA DO COMPUTADOR:")
            time.sleep(1)
            if(numeroAleatorio == 1):
                print(pedra)
                print(" ")
                time.sleep(2)
                print(divisao)
                print("COMPUTADOR venceu!")
                placarMaquina+= 1
            elif(numeroAleatorio == 2):
                print(papel)
                print(" ")
                time.sleep(2)
                print(divisao)
                print("HUMANO venceu!")
                placarHumano+= 1
        
        print(divisao)
        print("Continuar - 1")
        print(" ")
        print("Sair - 0")
        print(" ")
        escolhaContinuar = int(input("Sua escolha: "))
        
        if(escolhaContinuar == 0):
            print("Placar")
            print(f"H - {placarHumano} X M - {placarMaquina}")
            infinito = 0
elif(escolhaModalidade == 3):
    print("Nada ainda...")
