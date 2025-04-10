# %%

import pandas as pd

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"
dfs = pd.read_html(url)
dfs

type(dfs)

# %%

df_uf = dfs[1]
df_uf.to_csv("ufs.csv", index=False)

df_ufs = pd.read_csv("ufs.csv")
df_ufs