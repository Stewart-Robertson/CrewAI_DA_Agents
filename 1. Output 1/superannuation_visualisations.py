import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the dataset
file_path = 'Superannuation.csv'
df = pd.read_csv(file_path)

# Create output directory if not exists
output_dir = 'visualisation_reports'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

plt.style.use('seaborn-whitegrid')

# Define color palettes
color_palette = sns.color_palette('Set2')

# 1. Gender Distribution
plt.figure(figsize=(8,6))
ax = sns.countplot(data=df, x='gender', palette=color_palette)
plt.title('Gender Distribution of Members')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
png1 = os.path.join(output_dir, 'gender_distribution.png')
plt.savefig(png1)
plt.close()

# 2. Employment Status Distribution
plt.figure(figsize=(8,6))
ax = sns.countplot(data=df, x='employment_status', palette=color_palette)
plt.title('Employment Status Distribution')
plt.xlabel('Employment Status')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
png2 = os.path.join(output_dir, 'employment_status_distribution.png')
plt.savefig(png2)
plt.close()

# 3. Salary Distribution
plt.figure(figsize=(8,6))
sns.histplot(df['salary'].dropna(), bins=30, kde=True, color=color_palette[3])
plt.title('Salary Distribution of Members')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.tight_layout()
png3 = os.path.join(output_dir, 'salary_distribution.png')
plt.savefig(png3)
plt.close()

# 4. Super Balance Distribution (Boxplot)
plt.figure(figsize=(8,6))
sns.boxplot(x=df['super_balance'], color=color_palette[2])
plt.title('Super Balance Distribution (Boxplot)')
plt.xlabel('Super Balance')
plt.tight_layout()
png4 = os.path.join(output_dir, 'super_balance_boxplot.png')
plt.savefig(png4)
plt.close()

# 5. Super Balance Distribution (Histogram)
plt.figure(figsize=(8,6))
sns.histplot(df['super_balance'].dropna(), bins=30, kde=True, color=color_palette[1])
plt.title('Super Balance Distribution')
plt.xlabel('Super Balance')
plt.ylabel('Frequency')
plt.tight_layout()
png5 = os.path.join(output_dir, 'super_balance_distribution.png')
plt.savefig(png5)
plt.close()

# 6. Contribution Rates: Employee vs Employer scatter
plt.figure(figsize=(8,6))
plt.scatter(df['employee_contribution_rate'], df['employer_contribution_rate'], c=color_palette[4], alpha=0.6)
plt.title('Employer vs Employee Contribution Rates')
plt.xlabel('Employee Contribution Rate')
plt.ylabel('Employer Contribution Rate')
plt.tight_layout()
png6 = os.path.join(output_dir, 'contribution_rates_comparison.png')
plt.savefig(png6)
plt.close()

# 7. Investment Options Distribution
plt.figure(figsize=(8,6))
ax = sns.countplot(data=df, x='investment_option', palette=color_palette)
plt.title('Investment Options Distribution')
plt.xlabel('Investment Option')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
png7 = os.path.join(output_dir, 'investment_options_distribution.png')
plt.savefig(png7)
plt.close()

# Prepare summary dictionary
summary = {
    'gender_distribution': 'Bar plot showing count of members by gender.',
    'employment_status_distribution': 'Bar plot showing count of members by employment status.',
    'salary_distribution': 'Histogram with KDE showing distribution of member salaries.',
    'super_balance_boxplot': 'Boxplot indicating distribution and outliers in super balances.',
    'super_balance_distribution': 'Histogram with KDE of super balance distribution.',
    'contribution_rates_comparison': 'Scatter plot showing relationship between employer and employee contribution rates.',
    'investment_options_distribution': 'Bar plot showing count of members by investment option.'
}

# List of PNG files created
output_files = [png1, png2, png3, png4, png5, png6, png7]

if __name__ == '__main__':
    print('Visualisations saved in directory:', output_dir)
    print('Files:', output_files)
    print('Summary of visualisations:')
    for k,v in summary.items():
        print(f'{k}: {v}')

# Save summary dictionary and list files for user to return
import json
output_summary_file = os.path.join(output_dir, 'summary.json')
with open(output_summary_file, 'w') as f:
    json.dump({'files': output_files, 'summary': summary}, f, indent=4)
