# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv")
clientes

# %%

clientes.dropna(how="all")

# %%

df = pd.DataFrame(
    {
        "nome": ["João", None, "José", "Ana"],
        "idade": [25, None, 35, 40],
        "salario": [None, 3000, 4000, None],
    }
)

df.dropna(how="all", subset=["idade", "nome"])

# %%

df["idade"] = df["idade"].fillna("sem valor")
df

# %%

df.fillna({"nome": "alguém", "idade": "algum"})

# %%

medias = df[["idade", "salario"]].mean()
df.fillna(medias)

# %%

print(df["idade"].fillna(df["idade"].mean()).mean())