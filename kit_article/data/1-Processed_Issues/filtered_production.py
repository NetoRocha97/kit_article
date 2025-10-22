import pandas as pd
import os

output_dir = '1-Processed_Issues/filtered_not_test_per_project'
os.makedirs(output_dir, exist_ok=True)

df = pd.read_csv('1-Processed_Issues/processed_issues.csv')

df_not_tests = df[~df['file'].str.contains(r'test|tests|Test', case=False, na=False)]

df_not_tests.to_csv('1-Processed_Issues/filtered_not_test_processed_issues.csv', index=False)

projetos = df_not_tests['repo'].unique()

for projeto in projetos:
    df_projeto = df_not_tests[df_not_tests['repo'] == projeto]
    nome_limpo = projeto.replace("/", "_").replace("\\", "_")
    output_path = f'{output_dir}/filtered_NOT_test_{nome_limpo}.csv'
    df_projeto.to_csv(output_path, index=False)
    print(f"Arquivo salvo: {output_path}")
