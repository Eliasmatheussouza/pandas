# %%

import pandas as pd

df = pd.DataFrame(
    {
        "cliente": [1, 2, 3, 4, 5],
        "nome": ["Matheus", "Ana", "João", "Joel", "Marcos"]
    }
)

df_2 = pd.DataFrame(
    {
        "cliente": [1, 2, 3],
        "nome": ["Jorge", "Lucas", "Lara"],
        "idade": [32, 29, 31]
    }
)

df_3 = pd.DataFrame(
    {
        "idade": [32, 34, 19, 54, 33]
    }
)

# %%

dfs = [df, df_2]

pd.concat(dfs, ignore_index=True)

# %%

df_3 = df_3.sort_values(by="idade").reset_index(drop=True)
df_3

# %%

pd.concat([df, df_3], axis=1)