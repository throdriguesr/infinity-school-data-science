import pandas as pd

# lista com os nomes dos estados brasileiros (mesma ordem das siglas da UF)
estados = [
    "Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará",
    "Distrito Federal", "Espírito Santo", "Goiás", "Maranhão",
    "Mato Grosso", "Mato Grosso do Sul", "Minas Gerais", "Pará",
    "Paraíba", "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro",
    "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia", "Roraima",
    "Santa Catarina", "São Paulo", "Sergipe", "Tocantins"
]

# cria a série já com o nome "ESTADO"
serie_estado = pd.Series(estados, name="ESTADO")

# exibe a série
print("=== Série ESTADO ===")
print(serie_estado)