import pandas as pd

# lista com as siglas dos estados
ufs = [
    "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA",
    "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN",
    "RS", "RO", "RR", "SC", "SP", "SE", "TO"
]

# cria a série já com o nome "UF"
serie_uf = pd.Series(ufs, name="UF")

# exibe a série
print("=== Série UF ===")
print(serie_uf)