# %%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv")
df

df.shape
df.info(memory_usage='deep')
df.dtypes

# %%

df.rename(columns={"idCliente": "id_cliente"})

df["id_cliente"]

# %%

df[["id_cliente", "idTransacao"]].tail(5)

# %%

colunas = df.columns.tolist()
colunas.sort()
colunas

# %%

df = df[colunas]
df