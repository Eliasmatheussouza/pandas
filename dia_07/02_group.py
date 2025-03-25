# %%

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv")
transacoes.head()

# %%

transacoes.groupby(by=["idCliente"], as_index=False)[["idTransacao"]].count()