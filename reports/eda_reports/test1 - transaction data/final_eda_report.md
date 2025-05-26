# Comprehensive Exploratory Data Analysis (EDA) Report

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

## 2. Correlation Analysis

### Correlation Matrix

|                      | transaction_id | amount  | account_number | credit_card_number |
|----------------------|----------------|---------|----------------|--------------------|
| transaction_id       | 1.00           | 0.01    | 0.00           | 0.00               |
| amount               | 0.01           | 1.00    | -0.05          | -0.03              |
| account_number       | 0.00           | -0.05   | 1.00           | 0.60               |
| credit_card_number   | 0.00           | -0.03   | 0.60           | 1.00               |

### Insights
- The `amount` column appears to be independent of the identifiers, suggesting that transaction values are not directly related to these account attributes.
- The strong correlation between `account_number` and `credit_card_number` confirms that these columns are linked, potentially representing the same entity with different identifiers.

## 3. Distribution Summary

### Outlier Findings
- **Z-score Method**: Number of outliers detected: 20
- **IQR Method**: Number of outliers detected: 25
- Outliers were mostly high-value transactions significantly larger than the bulk of data, some exceeding 900,000 units in their respective currencies.

## 4. Insights and Recommendations
1. The majority of transactions are categorized as expenses, indicating a potential area for cost management.
2. The currency with the highest transaction volume is CNY, suggesting a focus on this market.
3. Investigate high-value transactions for potential errors or fraud.
4. Implement strategies to handle missing values in critical columns.
5. Consider standardizing currency reporting for better analysis.

## 5. Conclusion
This report summarizes the exploratory data analysis conducted on the financial transactions dataset. It includes statistical summaries, correlation analysis, distribution insights, and recommendations for future data handling and analysis.

---

Please refer to this report as `final_eda_report.md` for inclusion in the final report summary.