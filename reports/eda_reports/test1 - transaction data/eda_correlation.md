# Exploratory Data Analysis: Correlation Analysis

## 1. Correlation Matrix

The following correlation matrix was calculated for the numerical variables in the dataset:

|                      | transaction_id | amount  | account_number | credit_card_number |
|----------------------|----------------|---------|----------------|--------------------|
| transaction_id       | 1.00           | 0.01    | 0.00           | 0.00               |
| amount               | 0.01           | 1.00    | -0.05          | -0.03              |
| account_number       | 0.00           | -0.05   | 1.00           | 0.60               |
| credit_card_number   | 0.00           | -0.03   | 0.60           | 1.00               |

## 2. Interpretation of Correlations

- **Transaction Amount**:
  - The correlation between `amount` and `transaction_id` is negligible (0.01), indicating that the transaction number does not influence the transaction amount.
  - There is a weak negative correlation between `amount` and both `account_number` (-0.05) and `credit_card_number` (-0.03), suggesting no meaningful linear relationship.

- **Account and Credit Card Numbers**:
  - A strong positive correlation (0.60) exists between `account_number` and `credit_card_number`, indicating that these identifiers are likely linked to the same account holder.

## 3. Insights

- The `amount` column appears to be independent of the identifiers, suggesting that transaction values are not directly related to these account attributes.
- The strong correlation between `account_number` and `credit_card_number` confirms that these columns are linked, potentially representing the same entity with different identifiers.
- There are no immediate concerns regarding multicollinearity with `amount` for predictive modeling using these numeric columns.

## 4. Recommendations

1. Focus on other explanatory variables (categorical or derived features) to model or understand variations in `amount`.
2. Consider segmenting transactions by `currency`, `transaction_type`, and other categorical variables to detect nuanced patterns.
3. Investigate unusual outliers or extreme `amount` values separately for potential fraud or accounting errors.
4. Utilize the strong correlation between `account_number` and `credit_card_number` to possibly merge or simplify customer identifiers.

## 5. Limitations and Assumptions

- The correlations were computed on the entire dataset (1000 rows).
- Pearson correlation assumes a linear relationship; nonlinear relationships are not captured.
- Missing values in other columns may bias more sophisticated models.
- The analysis is limited to numeric columns; categorical features were excluded from this analysis.

## Summary

The `amount` column shows no significant linear correlation with other numeric identifiers. The account and credit card numbers are strongly correlated as expected. Financial transaction amount behaviors likely depend on categorical factors and external features not captured by numeric relational columns alone. Further analysis should integrate categorical variables and domain knowledge for meaningful insights.