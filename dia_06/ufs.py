# %%

import pandas as pd

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

dfs = pd.read_html(url)
ufs = dfs[1]

# %%

ufs.dtypes
# %%

def str_to_float(x:str):
    x = (x.replace(",", ".")
         .replace(" ", "")
         .replace("\xa0", "")
        )
    return float(x)

# %%

ufs["Área (km²)"] = ufs["Área (km²)"].apply(str_to_float)

ufs["PIB per capita (R$) (2015)"] = ufs["PIB per capita (R$) (2015)"].apply(str_to_float)

ufs["População (Censo 2022)"] = ufs["População (Censo 2022)"].apply(str_to_float)

ufs["PIB (2015)"] = ufs["PIB (2015)"].apply(str_to_float)

# %%

ufs.dtypes

# %%

linha = ufs.iloc[4]

# %%

def classifica_bom(linha):
    (linha["Área (km²)"] > 100000 and
    linha["PIB per capita (R$) (2015)"] > 15000 and
    linha["IDH (2010)"] > 0.7)

# %%

ufs.apply(classifica_bom, axis=1)