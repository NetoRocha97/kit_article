import pandas as pd

df = pd.read_csv('1-Processed_Issues/processed_issues.csv')

df_tests = df[df['file'].str.contains(r'test|tests|Test', case=False, na=False)]

print(df_tests.head())

df_tests.to_csv('1-Processed_Issues/filtered_test_processed_issues.csv', index=False)

print("Arquivo filtrado salvo como '1-Processed_Issues/1_filtered_test_issues.csv'")
