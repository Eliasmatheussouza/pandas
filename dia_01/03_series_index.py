# %%
import pandas as pd

idade = [
    18, 22, 15, 50, 30,
    35, 40, 45, 50, 55,
    90, 95, 100, 105, 110
]

series_idade = pd.Series(idade)
print(series_idade)

# %%

idade[0]