import pandas as pd

# Carregar o arquivo filtrado
filtered = pd.read_csv('1-Processed_Issues/filtered_test_processed_issues.csv')

# Carregar o arquivo de monitoramento
prs_monitoring = pd.read_csv('2-Prs_Monitoring/prs_monitoring.csv')

# Chave de filtragem
chave = 'pr_number'

# Criar um conjunto com os pr_numbers filtrados
pr_numbers_filtrados = set(filtered[chave].unique())

# Filtrar o arquivo de monitoramento
filtered_monitoring = prs_monitoring[prs_monitoring[chave].isin(pr_numbers_filtrados)]

# Salvar o arquivo filtrado
filtered_monitoring.to_csv('2-Prs_Monitoring/2_filtered_test_prs_monitoring.csv', index=False)
