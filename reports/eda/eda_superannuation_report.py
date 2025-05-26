import pandas as pd
import numpy as np

# Load dataset
file_path = 'Superannuation.csv'
data = pd.read_csv(file_path, nrows=500)

# Selecting relevant numerical columns for correlation analysis
numerical_cols = ['salary', 'employer_contribution_rate', 'employee_contribution_rate', 'super_balance']

# Checking for missing values in selected columns
missing_values = data[numerical_cols].isnull().sum()

# Handle missing values by dropping rows with missing values for correlation calculation
data_filtered = data[numerical_cols].dropna()

# Calculate correlation matrix
correlation_matrix = data_filtered.corr()

# Format correlation matrix for markdown output
corr_markdown = correlation_matrix.to_markdown(floatfmt='.3f')

# Generate insights based on correlation values
def generate_insights(corr):
    insights = []
    if corr.loc['salary', 'super_balance'] > 0.3:
        insights.append("There is a moderate positive correlation between salary and super balance, indicating that higher salaries tend to be associated with higher super balances.")
    if corr.loc['salary', 'employer_contribution_rate'] > 0.3:
        insights.append("Employer contribution rate moderately correlates positively with salary, suggesting employers may contribute more for higher salary earners.")
    if abs(corr.loc['employee_contribution_rate', 'salary']) < 0.2:
        insights.append("Employee contribution rate shows weak or no significant correlation with salary or super balance, indicating varied employee contribution behaviors.")
    if corr.loc['employer_contribution_rate', 'super_balance'] < 0.2:
        insights.append("The employer contribution rate has a weak correlation with super balance, possibly due to other factors influencing super balance accumulation.")
    return insights

insights = generate_insights(correlation_matrix)

# Create markdown report
report = f"""
# Exploratory Data Analysis on Superannuation Dataset

## Introduction
This report presents the exploratory data analysis (EDA) conducted on the Superannuation dataset to identify correlations among key numerical variables, patterns, and insights. The dataset contains information on members' salaries, employer and employee contribution rates, and superannuation balances.

## Data Summary
- Total Rows Analyzed: {len(data_filtered)}
- Numerical Columns:
    - Salary
    - Employer Contribution Rate
    - Employee Contribution Rate
    - Super Balance

## Missing Values
```
{missing_values}
```

## Correlation Matrix
```
{corr_markdown}
```

## Insights