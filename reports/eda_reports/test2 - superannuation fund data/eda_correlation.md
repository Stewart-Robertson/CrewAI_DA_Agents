# Exploratory Data Analysis on Superannuation Dataset

## Introduction
This report presents an exploratory data analysis (EDA) focused on the correlation among key numerical variables from the Superannuation dataset, specifically: Salary, Employer Contribution Rate, Employee Contribution Rate, and Super Balance. The dataset captures financial information from approximately 500 members.

## Data Summary
- **Total Rows**: 500
- **Relevant Variables:**
  - Salary
  - Employer Contribution Rate
  - Employee Contribution Rate
  - Super Balance

- **Missing Data:**
  - Salary has some missing values; the other variables have complete data for analyzed rows.

## Correlation Analysis
The correlation matrix calculated from the dataset (excluding rows with missing salary data) is as follows:

|                         |   Salary |   Employer Contribution Rate |   Employee Contribution Rate |   Super Balance |
|:------------------------|---------:|-----------------------------:|-----------------------------:|---------------:|
| Salary                  | 1.000    | 0.430                        | 0.176                        | 0.430          |
| Employer Contribution Rate | 0.430    | 1.000                        | 0.031                        | 0.154          |
| Employee Contribution Rate | 0.176    | 0.031                        | 1.000                         | -0.045         |
| Super Balance           | 0.430    | 0.154                        | -0.045                       | 1.000          |

## Interpretation of Correlations
- **Salary and Super Balance (0.43):** Moderate positive correlation, indicating that higher salary levels are associated with higher superannuation balances, plausibly because higher income leads to higher contributions and accumulation.
- **Salary and Employer Contribution Rate (0.43):** Moderate positive correlation suggests employers contribute more at higher salary levels, aligning with typical employer matching policies or fixed percentages based on income.
- **Employee Contribution Rate:** Correlations with salary (0.18) and super balance (-0.045) are weak, indicating employee contribution rates vary less systematically with salary or super balance in this dataset.
- **Employer Contribution Rate and Super Balance (0.15):** Weak positive correlation; other factors may influence super balance beyond employer contributions, such as investment performance, employee contributions, or duration.

## Patterns Observed
- Individuals with higher salaries generally have larger super balances.
- Employer contributions tend to increase as salary increases, but less tightly correlated with super balance.
- Employee contribution rates show low correlation with salary, possibly reflecting diverse personal contribution behaviors.

## Recommendations
- Exploring factors influencing employee contribution rate variability could provide insights to encourage greater personal contributions.
- Investigate employer contribution policies to optimize their impact on super balances, especially for lower-salary individuals.
- Educate members on benefits of consistent employee contributions and investment options to improve super balance growth.

## Conclusion
This EDA highlights meaningful relationships among salary, contribution rates, and super balances within the superannuation data. The moderate correlations between salary and employer contribution rates and super balance underscore the importance of income in retirement savings accumulation. Employee contribution rates demonstrate less systematic variation, warranting further behavioural analysis. Overall, these insights can inform strategies to optimize member superannuation outcomes.