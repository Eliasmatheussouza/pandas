# %%

import pandas as pd

df = pd.read_csv("../data/clientes.csv")
df.head()

# %%

idClientes = "000ff655-fa9f-4baa-a108-47f581ec52a1"

def get_last_id(x):
    return x.split("-")[-1]

# %%

get_last_id("0033b737-8235-4c0f-9801-dc4ca185af00")

# %%

id_novo = []
for i in df["idCliente"]:
    novo = get_last_id(i)
    id_novo.append(novo)

df["novo_id"] = id_novo
df.head()

# %%

df["idCliente"].apply(get_last_id)