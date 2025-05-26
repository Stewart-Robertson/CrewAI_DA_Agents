# Missing Value Handling Strategy

## Missing Value Analysis
- **currency**: 37 missing values (3.7%)
- **account_type**: 49 missing values (4.9%)
- **merchant_name**: 45 missing values (4.5%)

## Handling Strategy
- **Imputation**: For `currency`, `account_type`, and `merchant_name`, impute missing values based on business rules or the most common values.
- **Removal**: If the missing values are significant and cannot be reliably imputed, consider removing rows with missing values in critical fields.