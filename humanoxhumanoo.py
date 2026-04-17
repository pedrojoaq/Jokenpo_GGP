def jogar_pedra_papel_tesoura():
    
    pontos_j1 = 0
    pontos_j2 = 0
    empates = 0
    
    print("--- Bem-vindo ao Jokenpô Humano x Humano! ---")
    print("Opções: pedra, papel, tesoura")

    while True:
        
        j1 = input("\nJogador 1, sua vez: ").lower().strip()
        j2 = input("Jogador 2, sua vez: ").lower().strip()
        
      
        opcoes = ["pedra", "papel", "tesoura"]
        if j1 not in opcoes or j2 not in opcoes:
            print("Entrada inválida! Tente novamente.")
            continue

        
        if j1 == j2:
            print(f"Empate! Ambos escolheram {j1}.")
            empates += 1
        elif (j1 == "pedra" and j2 == "tesoura") or \
             (j1 == "papel" and j2 == "pedra") or \
             (j1 == "tesoura" and j2 == "papel"):
            print(f"Jogador 1 venceu! {j1} ganha de {j2}.")
            pontos_j1 += 1
        else:
            print(f"Jogador 2 venceu! {j2} ganha de {j1}.")
            pontos_j2 += 1
            
        
        continuar = input("\nQuerem jogar novamente? (s/n): ").lower().strip()
        if continuar != 's':
            break

    # Placar Final
    print("\n" + "="*20)
    print("   PLACAR GERAL   ")
    print("="*20)
    print(f"Jogador 1: {pontos_j1}")
    print(f"Jogador 2: {pontos_j2}")
    print(f"Empates:   {empates}")
    print("="*20)
    print("Obrigado por jogar!")


jogar_pedra_papel_tesoura()
