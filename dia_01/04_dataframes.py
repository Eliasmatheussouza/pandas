# %%

import pandas as pd

idade = [
    18, 22, 15, 50, 30,
    35, 40, 45, 50, 55,
    90, 95, 100, 105, 110
]

nomes = ["João", "Maria", "Maria", "Pedro",
           "Ana", "Carla", "Paulo", "Lucas",
           "Marta", "Joaquim", "Ricardo", "Mariana",
              "Lúcia", "Teresa", "Rafael"
]

series_idades = pd.Series(idade)
series_nomes = pd.Series(nomes)

# %%

df = pd.DataFrame()
df["idade"] = series_idades
df["nomes"] = series_nomes
df

type(series_idades)

# %%

df["idade"]

print(df.iloc[0]["nomes"])
print(df.iloc[0])