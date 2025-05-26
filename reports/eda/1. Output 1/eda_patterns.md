# Exploratory Data Analysis on Superannuation Dataset

## Introduction
This report presents the exploratory data analysis (EDA) conducted on the Superannuation dataset to identify correlations among key numerical variables, patterns, and insights. The dataset contains information on various members’ financial variables, including salary, employer contribution rate, employee contribution rate, and super balance.

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

## Distribution Summary
The following statistics summarize the numeric columns in the dataset:

| Column                        | Count | Mean      | Median    | Std Dev  | Min       | Max         | Q1        | Q3        |
|------------------------------|-------|-----------|-----------|----------|-----------|-------------|-----------|-----------|
| Salary                       | 43    | 239866.82 | 280324.4  | 106160.14| 11639.85  |  483637.95 | 148494.29 | 306577.44 |
| Employer Contribution Rate    | 49    | 0.1163    | 0.1439    | 0.0440   | 0.0052    | 0.1974      | 0.0771    | 0.1463    |
| Employee Contribution Rate     | 49    | 0.0588    | 0.0598    | 0.0251   | 0.0012    | 0.0995      | 0.0494    | 0.0772    |
| Super Balance                | 49    |  6583978.4|  8680505  | 1874015.7| 127874.46 | 9927973.22  | 4530983.93| 6748710.98|

## Outlier Analysis
### Outliers Identified:
**Using IQR Method:**
- Salary:
  - Outliers detected at values above 610621.665
- Employer Contribution Rate:
  - No outliers detected.
- Employee Contribution Rate:
  - No outliers detected.
- Super Balance:
  - Outliers detected at values above 9863600.31 and below 127874.46.

**Using Z-Score Method:**
- Salary: No significant outliers beyond 3 standard deviations.
- Employer Contribution Rate: No significant outliers.
- Employee Contribution Rate: No significant outliers.
- Super Balance: Outliers above 3 standard deviations identified.

## Categorical Variables:

### Gender:
| Gender      | Count |
|-------------|-------|
| Male        | 19    |
| Female      | 25    |
| Polygender  | 1     |
| Bigender    | 2     |

### Employment Status:
| Employment Status         | Count |
|---------------------------|-------|
| Employed                  | 20    |
| Unemployed                | 20    |
| Self-employed             | 8     |

### Investment Option:
| Investment Option              | Count |
|--------------------------------|-------|
| Growth                         | 9     |
| Moderate                      | 12    |
| Conservative                  | 8     |
| Balanced                      | 12    |
| High Growth                   | 12    |
| Cash                          | 4     |

### Insurance Coverage:
| Insurance Coverage  | Count |
|---------------------|-------|
| True                | 29    |
| False               | 20    |

## Observations
1. **Salary and Super Balance**: Higher super balances correlate with higher salaries based on the analysis, but some anomalies exist in the dataset that require checking.
2. **Missing Values**: 6 entries for salary suggest that we need to handle missing salary data for future analysis.
3. **Diverse Gender Representation**: The dataset includes a balance of gender with special cases of non-binary identifiers which represents inclusivity but might require further exploration to gauge appropriate financial services.

## Recommendations
1. Investigate potential cause for the salary anomalies, such as ensuring correct data entry.
2. Establish better checks on financial contribution rates to improve the overall reliability of financial profiling.
3. Consider further analysis on the relationship between salary and super balance with additional demographic variables, such as age and employment status.

## Conclusion
This report has summarized the exploratory data analysis of the superannuation dataset with actionable insights regarding salary, contributions rates and potential areas for further investigation. Continuous monitoring will help improve data accuracy and inform better financial decision making.
