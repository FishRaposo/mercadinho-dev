produtos = []


def salvar_produto(nome, preco, quantidade):
    produtos.append(
        {
            "nome": nome,
            "preco": preco,
            "estoque": quantidade,
        }
    )


def buscar_produto(nome):
    nome_procurado = nome.casefold()
    for produto in produtos:
        if produto["nome"].casefold() == nome_procurado:
            return produto
    return None


def listar_produtos():
    return produtos


def atualizar_estoque(produto, diferenca):
    produto["estoque"] += diferenca
