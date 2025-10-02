import pandas as pd

# lista com siglas
ufs = [
    "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA",
    "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN",
    "RS", "RO", "RR", "SC", "SP", "SE", "TO"
]

# lista com nomes dos estados
estados = [
    "Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará",
    "Distrito Federal", "Espírito Santo", "Goiás", "Maranhão",
    "Mato Grosso", "Mato Grosso do Sul", "Minas Gerais", "Pará",
    "Paraíba", "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro",
    "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia", "Roraima",
    "Santa Catarina", "São Paulo", "Sergipe", "Tocantins"
]

# lista com populações aproximadas (IBGE 2022, em milhões)
populacoes = [
    0.9, 3.4, 0.9, 3.9, 15.1, 9.2, 3.0, 4.1, 7.2, 7.1,
    3.7, 2.8, 20.5, 9.0, 4.0, 11.6, 9.7, 3.3, 17.3, 3.6,
    11.3, 1.8, 0.6, 7.6, 46.0, 2.4, 1.6
]

# cria o DataFrame usando dicionário
df = pd.DataFrame({
    "UF": ufs,
    "ESTADO": estados,
    "POPULAÇÃO (milhões)": populacoes
})

# exibe o DataFrame
print("=== DataFrame UF | ESTADO | POPULAÇÃO ===")
print(df)