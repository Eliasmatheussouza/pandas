# %%

import pandas as pd

df = pd.read_csv("../data/clientes.csv")
df

# %%

df.to_csv("clientes.csv", index=False)

# %%

df.to_parquet("clientes.parquet", index=False)
df

# %%

df_2 = pd.read_parquet("clientes.parquet")
df_2

# %%

df.to_excel("clientes.xlsx", index=False)
df

# %%

df_3 = pd.read_csv("teste.csv", sep=";")
df_3.to_csv("teste.csv", sep=";", index=False)
df_3