import math

import dados


def cadastrar_produto(nome, preco, quantidade):
    nome = nome.strip()

    if not nome:
        return "Nome inválido."
    if (
        not isinstance(preco, (int, float))
        or not math.isfinite(preco)
        or preco < 0
    ):
        return "O preço deve ser um valor não negativo."
    if not isinstance(quantidade, int) or quantidade < 0:
        return "A quantidade em estoque deve ser um inteiro não negativo."
    if dados.buscar_produto(nome) is not None:
        return "Já existe um produto com esse nome."

    dados.salvar_produto(nome, float(preco), quantidade)
    return "Produto cadastrado com sucesso."


def obter_produtos():
    return dados.listar_produtos()


def vender_produto(nome, quantidade, saldo):
    produto = dados.buscar_produto(nome.strip())
    if produto is None:
        return "Produto não encontrado."
    if not isinstance(quantidade, int) or quantidade <= 0:
        return "A quantidade da venda deve ser um inteiro maior que zero."
    if (
        not isinstance(saldo, (int, float))
        or not math.isfinite(saldo)
        or saldo < 0
    ):
        return "O saldo disponível deve ser um valor não negativo."
    if produto["estoque"] < quantidade:
        return "Estoque insuficiente."

    total = produto["preco"] * quantidade
    if saldo < total:
        return f"Saldo insuficiente. Total da compra: R$ {total:.2f}."

    dados.atualizar_estoque(produto, -quantidade)
    return (
        f"Venda realizada com sucesso. Total: R$ {total:.2f}. "
        f"Estoque restante: {produto['estoque']}."
    )
