# %%

import pandas as pd

def_clientes = pd.read_csv("clientes.csv")
print(def_clientes)

# %%

def_clientes.head(n=10)

# %%

def_clientes.tail(2)

# %%

def_clientes.sample(5)

# %%

def_clientes.shape

# %%

def_clientes.columns

# %%

def_clientes.index

# %%

def_clientes.info(memory_usage="deep", max_cols=5)

# %%

def_clientes.dtypes["idCliente"]