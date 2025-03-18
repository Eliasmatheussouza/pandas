# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv")

max_pontos = clientes["qtdePontos"].max()
filtro = clientes["qtdePontos"] == max_pontos
clientes[filtro]

# %%

top_5 = (clientes.sort_values(by = "qtdePontos", ascending = False)
         .head(5)["idCliente"])

top_5

# %%

brinquedo = pd.DataFrame(
    {
    "nome": ["Matheus", "Lucas", "Pedro", "João", "Maria"],
    "idade": [10, 12, 11, 9, 10],
    "salario": [22000, 1200, 1100, 900, 1000],
    }
)

brinquedo
# %%

brinquedo.sort_values(by = ["salario", "idade"], ascending = [False, True])
# %%
