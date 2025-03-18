# %%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv")
df.head()

# %%

pontos = [10, 1, 1, 1, 50, 100, 130, 30, 25, 50]
filtro = []

valores_50_mais = []
for i in pontos:
    if i >= 50:
        filtro.append(i>=50)

filtro

# %%

resultado = []