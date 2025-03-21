# %%

import pandas as pd

# %%

df = pd.DataFrame(
    {
        "nome": ["Matheus", "João", "Maria", "João", "Silvia"],
        "sobrenome": ["Souza", "Souza", "Santos", "Souza", "Silva"],
        "salario": [1000, 2000, 3000, 2000, 5000]
    }
)
df

# %%

df.drop_duplicates(keep="last")

# %%

df = (df.sort_values("salario", ascending=False)
        .drop_duplicates(subset=["nome", "sobrenome"]))