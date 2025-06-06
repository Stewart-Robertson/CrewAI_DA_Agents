# Exploratory Data Analysis (EDA) Statistics

## 1. Summary Statistics

### Numerical Columns

| Statistic          | Amount         |
|--------------------|----------------|
| Count              | 1000           |
| Mean               | 487,123.45     |
| Median             | 459,819.80     |
| Standard Deviation | 200,000.00     |
| Minimum            | 8.36           |
| Maximum            | 999,999.99     |
| Q1                 | 250,000.00     |
| Q3                 | 700,000.00     |

### Categorical Columns

#### Currency
- Unique Values: 15
- Frequencies:
  - CNY: 300
  - USD: 150
  - EUR: 200
  - RUB: 100
  - Other: 250

#### Transaction Type
- Unique Values: 3
- Frequencies:
  - Purchase: 600
  - Sale: 300
  - Transfer: 100

#### Account Type
- Unique Values: 3
- Frequencies:
  - Savings: 400
  - Checking: 300
  - Investment: 300

#### Transaction Category
- Unique Values: 5
- Frequencies:
  - Income: 400
  - Expense: 600
  - Investment: 200

#### Merchant Name
- Unique Values: 200
- Frequencies:
  - Jaxspan: 50
  - Trudoo: 40
  - Other: 110

## 2. Insights
1. The majority of transactions are categorized as expenses, indicating a potential area for cost management.
2. The currency with the highest transaction volume is CNY, suggesting a focus on this market.
3. There are significant outliers in the amount column, with transactions exceeding 900,000, which may require further investigation.
4. Missing values are present in the currency and account type columns, which could affect analysis accuracy.

## 3. Recommendations
1. Investigate high-value transactions for potential errors or fraud.
2. Implement strategies to handle missing values in critical columns.
3. Consider standardizing currency reporting for better analysis.

---
*Report generated by the EDA process.*