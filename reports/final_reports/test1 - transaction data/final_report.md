# Final Report

## 1. Data Cleaning Summary

### 1.1 Initial Data Assessment Results

#### Column Summary
- **transaction_id**: int
- **transaction_date**: str
- **amount**: float
- **currency**: str
- **transaction_type**: str
- **account_number**: int
- **account_type**: str
- **transaction_category**: str
- **merchant_name**: str
- **credit_card_number**: int

#### Data Quality Metrics
- **Total Rows**: 1000
- **Total Columns**: 10
- **Missing Values**:
  - currency: 37
  - account_type: 49
  - merchant_name: 45
- **Duplicate Count**: 0

### 1.2 Recommendations
1. Impute or handle missing values in currency, account type, and merchant name based on business rules.
2. Standardize date formats in transaction_date.
3. Review the categorization of currency and account_type for consistency.

### 1.3 Strategy for Handling Missing Values
- **Imputation**: For `currency`, `account_type`, and `merchant_name`, impute missing values based on business rules or the most common values.
- **Removal**: If the missing values are significant and cannot be reliably imputed, consider removing rows with missing values in critical fields.

### 1.4 Strategy for Standardizing Data Types
- **Transaction Date**: Convert to YYYY-MM-DD format.
- **Currency**: Impute or drop missing values based on the most frequent value.
- **Account Type**: Impute or drop missing values based on the most frequent value.
- **Merchant Name**: Impute or drop missing values based on the most frequent value.
- **Credit Card Number**: Convert to string format to handle leading zeros and missing values.

### 1.5 Strategy for Handling Outliers
- **Z-score Method**: Values with absolute Z-score greater than 3 were flagged as outliers.
- **IQR Method**: Outliers are values below Q1 - 1.5*IQR or above Q3 + 1.5*IQR.
- **Recommendations**:
  1. Winsorization (Capping): Cap outlier values to the nearest non-outlier bounds.
  2. Data Validation: Confirm transactions flagged as outliers are not errors.
  3. Imputation: For missing `amount` or critical fields, use median or domain-appropriate imputations.

---

## 2. Exploratory Data Analysis (EDA)

### 2.1 Summary Statistics

#### Numerical Columns
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

#### Categorical Columns
- **Currency**: Unique Values: 15
- **Transaction Type**: Unique Values: 3
- **Account Type**: Unique Values: 3
- **Transaction Category**: Unique Values: 5
- **Merchant Name**: Unique Values: 200

### 2.2 Insights
1. The majority of transactions are categorized as expenses, indicating a potential area for cost management.
2. The currency with the highest transaction volume is CNY, suggesting a focus on this market.
3. There are significant outliers in the amount column, with transactions exceeding 900,000, which may require further investigation.

### 2.3 Recommendations
1. Investigate high-value transactions for potential errors or fraud.
2. Implement strategies to handle missing values in critical columns.
3. Consider standardizing currency reporting for better analysis.

---

## 3. Visualisation Summary

### 3.1 Visualisation Types and Justifications
| Column Name          | Proposed Visualisation Type      | Justification |
|----------------------|---------------------------------|---------------|
| transaction_id       | Histogram                       | To show distribution and ensure uniqueness. |
| transaction_date     | Time Series Line Chart          | To observe transaction trends over time. |
| amount               | Histogram + Box Plot            | To highlight outliers and spread. |
| currency             | Bar Chart                      | To depict frequency of each currency. |
| transaction_type     | Bar Chart / Pie Chart          | For clear count comparison. |
| account_type         | Bar Chart                      | To show distribution across account types. |
| merchant_name        | Bar Chart with Top N + Others  | To reduce clutter while showing key merchants. |

### 3.2 Visualisation Files
- [Histogram of Transaction IDs](visualisation_reports/histogram_transaction_id.png)
- [Time Series of Transaction Dates](visualisation_reports/time_series_transaction_date.png)
- [Amount Histogram and Box Plot](visualisation_reports/amount_histogram_boxplot.png)
- [Bar Chart of Currency Frequencies](visualisation_reports/bar_chart_currency.png)
- [Bar Chart of Transaction Types](visualisation_reports/bar_chart_transaction_type.png)
- [Histogram of Account Numbers](visualisation_reports/histogram_account_number.png)
- [Bar Chart of Account Types](visualisation_reports/bar_chart_account_type.png)
- [Bar Chart of Transaction Categories](visualisation_reports/bar_chart_transaction_category.png)
- [Bar Chart of Top Merchants](visualisation_reports/bar_chart_merchant_name_top15_others.png)
- [Histogram of Credit Card Numbers](visualisation_reports/histogram_credit_card_number.png)

---

## 4. Critical Evaluation of Findings
The analysis reveals significant insights into the dataset, highlighting areas for improvement in data quality and analysis. The presence of missing values and outliers suggests a need for robust data handling strategies. The visualisations provide a clear representation of the data, aiding in understanding trends and distributions.

## 5. Actionable Recommendations
1. Implement data cleaning strategies as outlined in the data cleaning summary.
2. Regularly review and update the data handling processes to ensure data integrity.
3. Utilize the visualisations to inform business decisions and identify areas for further analysis.

## 6. Possibilities for Further Analysis
- Conduct a deeper analysis of high-value transactions to identify patterns or anomalies.
- Explore the impact of different currencies on transaction amounts and trends.
- Investigate the relationship between transaction types and categories to optimize financial strategies.