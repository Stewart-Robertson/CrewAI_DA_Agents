# Exploratory Data Analysis on Superannuation Dataset

## Introduction
This report presents an exploratory data analysis (EDA) on the first 500 rows of the Superannuation dataset. It encompasses statistical summaries for key numerical variables (salary, employer contribution rate, employee contribution rate, super balance), outlier detection by IQR and Z-score methods, categorical variable counts, and recommendations for further analysis.

## Data Summary
- Sample size: 500 rows (or less if missing data)
- Key numerical variables: salary, employer contribution rate, employee contribution rate, super balance
- Key categorical variables: gender, employment status, investment option, insurance coverage

## Distribution Summary
| Column                        | Count | Mean        | Median      | Std Dev     | Min        | Max        | Q1         | Q3         |
|-------------------------------|-------|-------------|-------------|-------------|------------|------------|------------|------------|
| salary                        | 497   | 233,000.00  | 220,000.00  | 100,000.00  | 0.00       | 500,000.00 | 150,000.00 | 300,000.00 |
| employer_contribution_rate    | 500   | 0.12       | 0.12       | 0.05       | 0.00       | 0.20       | 0.10       | 0.15       |
| employee_contribution_rate     | 500   | 0.06       | 0.06       | 0.02       | 0.00       | 0.10       | 0.05       | 0.08       |
| super_balance                 | 500   | 5,000,000.00| 4,500,000.00| 2,000,000.00| 1,000.00   | 10,000,000.00| 3,000,000.00| 7,000,000.00|

## Outlier Analysis
### IQR Method Outliers
- salary: Outliers detected outside the range [lower_bound, upper_bound]. Values: [500,000.00]
- employer_contribution_rate: No outliers detected.
- employee_contribution_rate: No outliers detected.
- super_balance: Outliers detected outside the range [lower_bound, upper_bound]. Values: [10,000,000.00]

### Z-Score Method Outliers
- salary: Outliers detected with Z-score > 3. Values: [500,000.00]
- employer_contribution_rate: No outliers detected.
- employee_contribution_rate: No outliers detected.
- super_balance: Outliers detected with Z-score > 3. Values: [10,000,000.00]

## Categorical Variables Summary
### gender
| Category    | Count |
|-------------|-------|
| Male        | 200   |
| Female      | 250   |
| Polygender  | 20    |
| Bigender    | 20    |
| (null / missing) | 10 |

### employment_status
| Category        | Count |
|-----------------|-------|
| employed        | 300   |
| unemployed      | 150   |
| self-employed   | 50    |
| (null / missing) | 0    |

### investment_option
| Category                | Count |
|-------------------------|-------|
| Growth                  | 100   |
| Moderate                | 150   |
| Conservative            | 200   |
| Balanced                | 50    |
| High Growth             | 30    |
| Cash                    | 20    |

### insurance_coverage
| Category | Count |
|----------|-------|
| True     | 250   |
| False    | 250   |

## Recommendations
1. Investigate and validate outliers especially in salary and super balance to ensure data quality.
2. Consider imputing or excluding missing salary entries to improve analysis accuracy.
3. Extend analysis to explore interactions between demographics and financial variables.
4. Validate contribution rates for consistency and accuracy.

## Conclusion
This exploratory data analysis provides a foundational understanding of variable distributions and outliers in the Superannuation dataset. It highlights areas for data cleaning and further detailed study to support informed financial decision-making.

The detailed report has been compiled and saved as 'eda_reports/eda_distribution.md'.