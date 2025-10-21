import pandas as pd

# Escolha o tipo de dado: 'train', 'val' ou 'test'
tipo = 'train'  # Altere para 'val' ou 'test' conforme necessário

# Caminhos de entrada e saída baseados no tipo
filtered_path = f'1-Processed_Issues/filtered_{tipo}_processed_issues.csv'
characterization_path = '3-Prs_Characterization/prs_characterization.csv'
output_path = f'3-Prs_Characterization/3_filtered_{tipo}_prs_characterization.csv'

# Chave de filtragem
chave = 'pr_number'

# Carregar os dados
filtered = pd.read_csv(filtered_path)
prs_characterization = pd.read_csv(characterization_path)

# Obter PRs filtrados
pr_numbers_filtrados = set(filtered[chave].unique())

# Filtrar caracterização
filtered_characterization = prs_characterization[prs_characterization[chave].isin(pr_numbers_filtrados)]

# Salvar resultado
filtered_characterization.to_csv(output_path, index=False)

print(f'Arquivo salvo em: {output_path}')
