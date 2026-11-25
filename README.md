# Mercadinho Dev

Sistema de linha de comando para cadastro de produtos, consulta de estoque e
realização de vendas. O projeto separa a apresentação, as regras de negócio e
os dados em três módulos Python.

## Requisitos

- Python 3

O projeto usa apenas a biblioteca padrão do Python.

## Como executar

No terminal, entre na pasta do projeto e execute:

```powershell
python main.py
```

O menu permite cadastrar um produto, listar produtos, realizar uma venda ou
sair. Ao cadastrar, informe o nome, o preço e a quantidade inicial. Ao vender,
informe o nome do produto, a quantidade desejada e o saldo disponível para a
compra.

## Regras

- Nomes de produtos não podem ficar vazios nem se repetir; a busca não diferencia
  maiúsculas de minúsculas.
- O preço deve ser finito e não negativo.
- A quantidade inicial deve ser um inteiro não negativo.
- A venda exige uma quantidade inteira maior que zero, estoque suficiente e
  saldo suficiente.
- O estoque só é reduzido quando a venda é aprovada.

## Estrutura

- `main.py`: menu, entradas e mensagens exibidas.
- `negocio.py`: validações e regras de cadastro e venda.
- `dados.py`: armazenamento em memória e operações sobre os produtos.

Os produtos são mantidos apenas em memória. Ao encerrar o programa, os dados
são perdidos. O saldo é informado para cada venda; o sistema não mantém contas
de clientes nem histórico de vendas.
