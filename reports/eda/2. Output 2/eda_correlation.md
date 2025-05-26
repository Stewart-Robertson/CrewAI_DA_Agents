# Exploratory Data Analysis on Superannuation Dataset

## Introduction
This report presents the exploratory data analysis (EDA) conducted on the Superannuation dataset to identify correlations among key numerical variables, patterns, and insights. The dataset contains information on members' salaries, employer and employee contribution rates, and superannuation balances.

## Data Summary
- Total Rows Analyzed: 487 (rows without missing values in selected numerical columns)
- Numerical Columns:
    - Salary
    - Employer Contribution Rate
    - Employee Contribution Rate
    - Super Balance

## Missing Values
```
salary                     56
employer_contribution_rate  0
employee_contribution_rate  0
super_balance               0
dtype: int64
```

## Correlation Matrix
```
|                         |   salary |   employer_contribution_rate |   employee_contribution_rate |   super_balance |
|:------------------------|---------:|-----------------------------:|-----------------------------:|---------------:|
| salary                  |     1    |                        0.430 |                        0.176 |           0.430 |
| employer_contribution_rate |     0.430 |                        1    |                        0.031 |           0.154 |
| employee_contribution_rate |     0.176 |                        0.031 |                        1    |          -0.045 |
| super_balance           |     0.430 |                        0.154 |                       -0.045 |           1    |
```

## Insights
- There is a moderate positive correlation between salary and super balance, indicating that higher salaries tend to be associated with higher super balances.
- Employer contribution rate moderately correlates positively with salary, suggesting employers may contribute more for higher salary earners.
- Employee contribution rate shows weak or no significant correlation with salary or super balance, indicating varied employee contribution behaviors.
- The employer contribution rate has a weak correlation with super balance, possibly due to other factors influencing super balance accumulation.

## Recommendations
1. Explore underlying factors affecting employee contribution rates to enhance understanding of their impact on super balances.
2. Investigate mechanisms linking employer contribution rates and salary increments to optimize employer-driven superannuation growth.
3. Consider integrating demographic and employment status factors in further analyses to enrich insights.

## Conclusion
The analysis indicates meaningful relationships between salary and super balance as well as employer contribution rates, while employee contributions show limited direct correlation. This suggests multi-faceted influences on superannuation balances requiring further exploration.