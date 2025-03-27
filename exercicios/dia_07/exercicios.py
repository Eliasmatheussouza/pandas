# %%

import pandas as pd

# %%

transacoes = pd.read_csv("../../data/transacoes.csv")
transacoes.head()

# %%

transacao_produto = pd.read_csv("../../data/transacao_produto.csv")
transacao_produto.head()

# %%

produtos = pd.read_csv("../../data/produtos.csv")
produtos.head()

# %%

cliente_transacao_produto = transacoes.merge(transacao_produto,
                                            on="idTransacao",
                                            how="left")

cliente_transacao_produto[["idTransacao", "idCliente", "idProduto"]]

cliente_transacao_produto.merge(produtos, on=["idProduto"])