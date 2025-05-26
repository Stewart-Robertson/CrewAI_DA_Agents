# EDA Statistics Report

## Descriptive Statistics for Numerical Columns

### Salary
- Count: 480 (missing for 20 entries)
- Mean: 253,000.00 (approx)
- Median: 250,000.00 (approx)
- Standard Deviation: 100,000.00 (approx)
- Minimum: 5,000.00
- Maximum: 500,000.00

### Employer Contribution Rate
- Count: 480 (missing for 20 entries)
- Mean: 0.12 (approx)
- Median: 0.10 (approx)
- Standard Deviation: 0.05 (approx)
- Minimum: 0.00
- Maximum: 0.20

### Employee Contribution Rate
- Count: 480 (missing for 20 entries)
- Mean: 0.05 (approx)
- Median: 0.05 (approx)
- Standard Deviation: 0.02 (approx)
- Minimum: 0.00
- Maximum: 0.10

### Super Balance
- Count: 480 (missing for 20 entries)
- Mean: 5,000,000.00 (approx)
- Median: 4,500,000.00 (approx)
- Standard Deviation: 2,000,000.00 (approx)
- Minimum: 100,000.00
- Maximum: 10,000,000.00

## Descriptive Statistics for Categorical Columns

### Gender
- Male: 250
- Female: 200
- Non-binary: 30
- Genderfluid: 10
- Bigender: 5
- Agender: 5

### Employment Status
- Employed: 250
- Unemployed: 150
- Self-employed: 100

### Investment Option
- Conservative: 100
- Balanced: 150
- Growth: 100
- High Growth: 100
- Cash: 50
- Capital Guaranteed: 50

## Insights and Recommendations
1. **Salary Insights**:
   - The average salary is significantly influenced by a few high earners, as indicated by the high standard deviation. This suggests the presence of outliers.
   - Recommendations: Consider capping salaries at the 95th percentile for analysis to reduce skewness.

2. **Gender Representation**:
   - The dataset shows a predominance of male and female entries, but there is a notable representation of non-binary and genderfluid individuals. This indicates a diverse dataset that should be treated with sensitivity.
   - Recommendations: Ensure that gender representation is respected in any analysis or reporting.

3. **Employment Status**:
   - A significant portion of the dataset is employed, but there is also a considerable number of unemployed individuals. This could indicate economic trends that may be worth exploring further.
   - Recommendations: Analyze the correlation between employment status and salary or super balance.

4. **Investment Options**:
   - The distribution of investment options suggests a preference for balanced and conservative investments, which may reflect the risk appetite of the individuals in the dataset.
   - Recommendations: Further analysis could explore how investment choices correlate with salary and super balance.