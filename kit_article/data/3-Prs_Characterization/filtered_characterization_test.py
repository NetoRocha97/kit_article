import pandas as pd

# Caminho corrigido para o CSV "not test"
filtered_path = r'C:\Users\Neto Rocha\Mestrado\Artigo base\filtro\1-Processed_Issues\filtered_not_test_processed_issues.csv'
characterization_path = r'C:\Users\Neto Rocha\Mestrado\Artigo base\filtro\3-Prs_Characterization\prs_characterization.csv'
output_path = r'C:\Users\Neto Rocha\Mestrado\Artigo base\filtro\3-Prs_Characterization\3_filtered_not_test_prs_characterization.csv'


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
