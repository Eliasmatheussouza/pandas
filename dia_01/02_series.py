# %%
idade = [
    18, 22, 15, 50, 30,
    35, 40, 45, 50, 55,
    90, 95, 100, 105, 110
]

media = sum(idade) / len(idade)
print("Média:", media)

diffs = 0
for i in idade:
    diffs += (i - media) ** 2

variancia = diffs / (len(idade) - 1)

print("Variancia:", variancia)

# %%
import pandas as pd
series_idade = pd.Series(idade)

print(series_idade)

# %%
media_idades = series_idade.mean()
var_idades = series_idade.var()
summmary_idades = series_idade.describe()

print(summmary_idades)
print(media_idades)
print(var_idades)