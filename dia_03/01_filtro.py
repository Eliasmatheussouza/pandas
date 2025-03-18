# %%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv")
df.head()

# %%

pontos = [10, True, True, True, 50, 100, 130, 30, 25, 50]
filtro = []

valores_50_mais = []
for i in pontos:
    if i >= 50:
        filtro.append(i>=50)

filtro

# %%

resultado = []
for i in range(len(pontos)):
    resultado.append(pontos[i] >= 50)

resultado
# %%

info = pd.DataFrame({"nome": ["matheus", "ana", "joão"],
                          "idade": [26, 25, 30],
                          "uf": ["RJ", "SP", "MG"]})

filtro = info["idade"] > 26
info[filtro]

# %%

df = pd.read_csv("../data/transacoes.csv")
df.head()

# %%

filtro = df["qtdePontos"] >= 50
df[filtro]

# %%

filtro = (df["qtdePontos"] >= 50) & (df["qtdePontos"] >= 100)
df[filtro]

# %%

filtro = (df["qtdePontos"] == True) | (df["qtdePontos"] == 100)
df[filtro]
