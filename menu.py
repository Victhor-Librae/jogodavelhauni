print("===== CAMPEONATO =====")
print("1-Jogar")
print("2-Ver regras")
print("3-Ver placar")
print("4-Sair")

vitorias_jogador = 0
vitorias_adversario = 0

opcao = input("Escolha uma opção:")

while opcao != "4":

    if opcao == "1":
        print("\nIniciar campeonato!")
        print("1 - Melhor de 3")
        print("2 - Melhor de 5")

        modo = input("Escolha o tipo de campeonato:")

        if modo == "1":
            print("Você escolheu Melhor de 3!")
        elif modo == "2":
            print("Você escolheu Melhor de 5!")
        else:
            print("Opção inválida,Digite Novamente")

    elif opcao == "2":
        print("\n===== REGRAS =====")
        print("Melhor de 3: vence quem ganhar 2 partidas.")
        print("Melhor de 5: vence quem ganhar 3 partidas.")

    elif opcao == "3":
        print("\n===== PLACAR =====")
        print("Vitórias do jogador:", vitorias_jogador)
        print("Vitórias do adversário:", vitorias_adversario)

    else:
        print("Opção inválida!")

    print("\n===== CAMPEONATO =====")
    print("1 - Jogar")
    print("2 - Ver regras")
    print("3 - Ver placar")
    print("4 - Sair")

    opcao = input("Escolha uma opção:")
    
print("Programa encerrado!")