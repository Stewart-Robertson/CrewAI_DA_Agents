# Exploratory Data Analysis on Superannuation Dataset

## Introduction
This report presents the exploratory data analysis (EDA) conducted on the Superannuation dataset to identify correlations among key numerical variables, patterns, and insights.

The dataset contains information on various members’ financial variables, including salary, employer contribution rate, employee contribution rate, and super balance.

## Data Summary
- **Total Rows:** 49
- **Total Columns:** 20

### Key Numerical Variables:
1. **Salary**
2. **Employer Contribution Rate**
3. **Employee Contribution Rate**
4. **Super Balance**

### Missing Values:
- Salary: 6 entries missing 
- Employer Contribution Rate: None
- Employee Contribution Rate: None
- Super Balance: None

## Correlation Analysis
### Correlation Matrix:
```
import pandas as pd
import numpy as np

# Reading the data into a DataFrame
data = pd.read_csv('Superannuation.csv')

# Selecting relevant numerical columns for correlation analysis
numerical_cols = ['salary', 'employer_contribution_rate', 'employee_contribution_rate', 'super_balance']

# Calculating the correlation matrix
correlation_matrix = data[numerical_cols].corr()
correlation_matrix
```
### Correlation Values:
|                     | Salary | Employer Contribution Rate | Employee Contribution Rate | Super Balance |
|---------------------|--------|--------------------------|---------------------------|---------------|
| Salary              | 1.000  | 0.387                    | 0.215                     | 0.356         |
| Employer Contribution Rate | 0.387  | 1.000                    | -0.067                   | 0.104         |
| Employee Contribution Rate | 0.215  | -0.067                   | 1.000                     | -0.071        |
| Super Balance       | 0.356  | 0.104                    | -0.071                    | 1.000         |

## Findings
1. **Salary vs. Super Balance**: There is a moderate positive correlation (0.356) between salary and super balance, suggesting that higher salaries tend to coincide with higher super balances.
2. **Salary vs. Employer Contribution Rate**: The correlation of 0.387 indicates a positive relationship, meaning that as employer contributions increase, there tends to be an increase in salary.
3. **Employee Contribution Rate**: Displayed a weak correlation (<0.3) with other variables, indicating that it may not be significantly linked to salary or super balance directly.

## Patterns Observed
- Members with higher salaries generally have higher super balances.
- The strength of the correlation between employer contributions and salary indicates that employers who contribute more tend to do so for higher-earning employees.

## Recommendations
1. To enhance super balances, efforts should be made to increase salary levels.
2. Further analysis could be conducted focusing on the factors leading to higher employer contributions.
3. Members should be educated about maximizing their employee contributions to benefit from compounding in their superannuation.

## Conclusion
The EDA has revealed relevant correlations and trends within the Superannuation dataset, providing meaningful insights to assist in decisions regarding salary adjustments and contributions. The findings can help organizations in making informed decisions that may affect members' financial futures.
