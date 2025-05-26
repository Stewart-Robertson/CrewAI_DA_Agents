import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime

# Create output directory
output_dir = 'visualisation_reports'
os.makedirs(output_dir, exist_ok=True)

# Load the first 500 rows
file_path = 'Superannuation.csv'
df = pd.read_csv(file_path, nrows=500)

# Convert date_of_birth to age
def calculate_age(birth_date):
    try:
        birth_date = pd.to_datetime(birth_date, errors='coerce')
        today = pd.Timestamp.today()
        age = (today - birth_date).days // 365
        return age
    except:
        return None

if 'date_of_birth' in df.columns:
    df['age'] = df['date_of_birth'].apply(calculate_age)
else:
    df['age'] = None

# Handle missing values
if 'salary' in df.columns:
    df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
    df['salary'].fillna(df['salary'].median(), inplace=True)

for col in ['employer_contribution_rate', 'employee_contribution_rate']:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
        df[col].fillna(0, inplace=True)

if 'super_balance' in df.columns:
    df['super_balance'] = pd.to_numeric(df['super_balance'], errors='coerce')
    df['super_balance'].fillna(df['super_balance'].median(), inplace=True)


def save_fig(fig, filename):
    fig.tight_layout()
    fig.savefig(os.path.join(output_dir, filename))
    plt.close(fig)

# Age distribution
if df['age'].notnull().sum() > 0:
    fig, axes = plt.subplots(1, 2, figsize=(12,5))
    sns.histplot(df['age'].dropna(), bins=20, ax=axes[0])
    axes[0].set_title('Age Distribution')
    sns.boxplot(x=df['age'], ax=axes[1])
    axes[1].set_title('Age Boxplot')
    save_fig(fig, 'age_distribution.png')

# Gender Distribution
if 'gender' in df.columns:
    fig, axes = plt.subplots(1, 2, figsize=(12,5))
    sns.countplot(x='gender', data=df, ax=axes[0])
    axes[0].set_title('Gender Distribution')
    axes[0].set_xlabel('Gender')
    counts = df['gender'].value_counts()
    axes[1].pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140)
    axes[1].set_title('Gender Distribution Pie Chart')
    save_fig(fig, 'gender_distribution.png')

# Employment Status
if 'employment_status' in df.columns:
    fig, axes = plt.subplots(1, 2, figsize=(12,5))
    sns.countplot(x='employment_status', data=df, ax=axes[0])
    axes[0].set_title('Employment Status Distribution')
    counts = df['employment_status'].value_counts()
    axes[1].pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140)
    axes[1].set_title('Employment Status Pie Chart')
    save_fig(fig, 'employment_status_distribution.png')

# Salary Distribution
if 'salary' in df.columns:
    fig, axes = plt.subplots(1, 3, figsize=(18,5))
    sns.histplot(df['salary'], bins=20, ax=axes[0])
    axes[0].set_title('Salary Distribution')
    sns.boxplot(x=df['salary'], ax=axes[1])
    axes[1].set_title('Salary Boxplot')
    sns.violinplot(x=df['salary'], ax=axes[2])
    axes[2].set_title('Salary Violin Plot')
    save_fig(fig, 'salary_distribution.png')

# Contribution rates
cols = ['employer_contribution_rate', 'employee_contribution_rate']
if all(c in df.columns for c in cols):
    fig, axes = plt.subplots(2, 2, figsize=(12,10))
    sns.histplot(df[cols[0]], bins=20, ax=axes[0,0])
    axes[0,0].set_title('Employer Contribution Rate Distribution')
    sns.boxplot(x=df[cols[0]], ax=axes[0,1])
    axes[0,1].set_title('Employer Contribution Rate Boxplot')
    sns.histplot(df[cols[1]], bins=20, ax=axes[1,0])
    axes[1,0].set_title('Employee Contribution Rate Distribution')
    sns.boxplot(x=df[cols[1]], ax=axes[1,1])
    axes[1,1].set_title('Employee Contribution Rate Boxplot')
    save_fig(fig, 'contribution_rates_comparison.png')

# Super Balance
if 'super_balance' in df.columns:
    fig, axes = plt.subplots(1, 3, figsize=(18,5))
    sns.histplot(df['super_balance'], bins=20, ax=axes[0])
    axes[0].set_title('Super Balance Distribution')
    sns.boxplot(x=df['super_balance'], ax=axes[1])
    axes[1].set_title('Super Balance Boxplot')
    sns.violinplot(x=df['super_balance'], ax=axes[2])
    axes[2].set_title('Super Balance Violin Plot')
    save_fig(fig, 'super_balance_distribution.png')

# Investment Option
if 'investment_option' in df.columns:
    fig, axes = plt.subplots(1, 2, figsize=(12,5))
    sns.countplot(x='investment_option', data=df, order=df['investment_option'].value_counts().index, ax=axes[0])
    axes[0].set_title('Investment Option Distribution')
    counts = df['investment_option'].value_counts()
    axes[1].pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140)
    axes[1].set_title('Investment Option Pie Chart')
    save_fig(fig, 'investment_option_distribution.png')

# Insurance Coverage
if 'insurance_coverage' in df.columns:
    fig, axes = plt.subplots(1, 2, figsize=(12,5))
    sns.countplot(x='insurance_coverage', data=df, ax=axes[0])
    axes[0].set_title('Insurance Coverage Distribution')
    counts = df['insurance_coverage'].value_counts()
    axes[1].pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140)
    axes[1].set_title('Insurance Coverage Pie Chart')
    save_fig(fig, 'insurance_coverage_distribution.png')

# Beneficiary Relationship
if 'beneficiary_relationship' in df.columns:
    fig, axes = plt.subplots(1, 2, figsize=(12,5))
    sns.countplot(x='beneficiary_relationship', data=df, order=df['beneficiary_relationship'].value_counts().index, ax=axes[0])
    axes[0].set_title('Beneficiary Relationship Distribution')
    counts = df['beneficiary_relationship'].value_counts()
    axes[1].pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140)
    axes[1].set_title('Beneficiary Relationship Pie Chart')
    save_fig(fig, 'beneficiary_relationship_distribution.png')

# City and State
if 'city' in df.columns and 'state' in df.columns:
    fig, axes = plt.subplots(1, 2, figsize=(14,10))
    sns.countplot(y='city', data=df, order=df['city'].value_counts().index, ax=axes[0])
    axes[0].set_title('City Distribution')
    sns.countplot(y='state', data=df, order=df['state'].value_counts().index, ax=axes[1])
    axes[1].set_title('State Distribution')
    save_fig(fig, 'city_state_distribution.png')

print('All visualisations created and saved to the visualisation_reports/ directory.')
