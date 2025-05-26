import pandas as pd

data = pd.read_csv('Superannuation.csv')
numerical_cols = ['salary', 'employer_contribution_rate', 'employee_contribution_rate', 'super_balance']

# Remove rows with missing values in numerical columns
clean_data = data.dropna(subset=numerical_cols)

correlation_matrix = clean_data[numerical_cols].corr()

print(correlation_matrix)

# Save to markdown
report = f"""# Superannuation Dataset Correlation Matrix\n\n"""
report += correlation_matrix.to_markdown()

with open('correlation_report.md', 'w') as f:
    f.write(report)