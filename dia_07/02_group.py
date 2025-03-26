# %%

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv")
transacoes.head()

# %%

transacoes.groupby(by=["idCliente"], as_index=False)[["idTransacao"]].count()

# %%

summary = (transacoes.groupby(by=["idCliente"], as_index=False)
                     .agg({"idTransacao": ["count"],
                           "qtdePontos": ["sum", "mean"]})
                    )

summary

# %%

summary[("qtdePontos", "mean")]

# %%

summary.columns = ["idCliente",
                   "qtdeTransacao",
                   "totalPontos",
                   "avgPontos"]
summary