jogos = []
carrinho = []

while True:
    menu = input(
        "\n[1] - Cadastrar jogo\n"
        "[2] - Adicionar ao carrinho\n"
        "[3] - Ver catálogo\n"
        "[4] - Buscar jogo\n"
        "[5] - Remover jogo\n"
        "[6] - Ver carrinho\n"
        "[7] - Sair\n"
        "Escolha: "
    ).strip()

    if menu == "1":
        cadastrar = input("Digite o nome do jogo: ").lower().strip()

        while cadastrar == "":
            print("Nome inválido!")
            cadastrar = input("Digite o nome do jogo: ").lower().strip()

        if cadastrar in jogos:
            print("Jogo já cadastrado!")
        else:
            jogos.append(cadastrar)
            print("Jogo cadastrado com sucesso!")

    elif menu == "2":
        pesquisa = input("Digite o nome do jogo: ").lower().strip()

        while pesquisa == "":
            print("Nome inválido!")
            pesquisa = input("Digite o nome do jogo: ").lower().strip()

        if pesquisa in jogos:
            carrinho.append(pesquisa)
            print("Jogo adicionado ao carrinho!")
        else:
            print("Jogo não encontrado no catálogo!")

    elif menu == "3":
        if not jogos:
            print("Nenhum jogo cadastrado!")
        else:
            print("\n=== CATÁLOGO ===")

            for jogo in jogos:
                print(f"- {jogo}")

    elif menu == "4":
        busca = input("Digite o nome do jogo: ").lower().strip()

        while busca == "":
            print("Nome inválido!")
            busca = input("Digite o nome do jogo: ").lower().strip()

        if busca in jogos:
            print("Jogo encontrado no catálogo!")
        else:
            print("Jogo não encontrado!")

    elif menu == "5":
        remover = input("Digite o nome do jogo para remover: ").lower().strip()

        while remover == "":
            print("Nome inválido!")
            remover = input("Digite o nome do jogo para remover: ").lower().strip()

        if remover in jogos:
            jogos.remove(remover)
            print("Jogo removido com sucesso!")
        else:
            print("Jogo não encontrado!")

    elif menu == "6":
        if not carrinho:
            print("Carrinho vazio!")
        else:
            print("\n=== CARRINHO ===")

            for item in carrinho:
                print(f"- {item}")

    elif menu == "7":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida!")
