import negocio


def ler_valor(mensagem):
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            return float(entrada)
        except ValueError:
            print("Digite um valor numérico válido.")


def ler_quantidade(mensagem):
    while True:
        entrada = input(mensagem).strip()
        try:
            return int(entrada)
        except ValueError:
            print("Digite uma quantidade inteira válida.")


def exibir_menu():
    print("\n=== Mercadinho Dev ===")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Realizar venda")
    print("4 - Sair")


def executar():
    while True:
        exibir_menu()
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            nome = input("Nome do produto: ")
            preco = ler_valor("Preço: R$ ")
            quantidade = ler_quantidade("Quantidade em estoque: ")
            print(negocio.cadastrar_produto(nome, preco, quantidade))
        elif opcao == "2":
            produtos = negocio.obter_produtos()
            if not produtos:
                print("Nenhum produto cadastrado.")
            else:
                print("\nProdutos em estoque:")
                for produto in produtos:
                    print(
                        f"- {produto['nome']}: R$ {produto['preco']:.2f} "
                        f"(estoque: {produto['estoque']})"
                    )
        elif opcao == "3":
            nome = input("Nome do produto: ")
            quantidade = ler_quantidade("Quantidade desejada: ")
            saldo = ler_valor("Saldo disponível do cliente: R$ ")
            print(negocio.vender_produto(nome, quantidade, saldo))
        elif opcao == "4":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    executar()
