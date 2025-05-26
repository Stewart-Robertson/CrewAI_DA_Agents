# Data Cleaning and Format Standardisation Report

## Overview
This report documents the analysis and cleaning strategy for the provided financial transaction dataset containing columns such as transaction_id, transaction_date, amount, currency, transaction_type, account_number, account_type, transaction_category, merchant_name, and credit_card_number.

---

## 1. Issues Identified and Inconsistent Formats

| Column               | Issue Description                      | Example of Inconsistent Entries          |
|----------------------|--------------------------------------|------------------------------------------|
| transaction_id       | Expected int, all valid               | N/A                                      |
| transaction_date     | Mixed date formats                    | "3/12/2020", "6/27/2022", "2020-03-15" |
| amount               | All valid floats                     | N/A                                      |
| currency             | Missing values (37)                   | Missing entries                          |
| transaction_type     | Valid strings                        | N/A                                      |
| account_number       | Expected int, valid                  | N/A                                      |
| account_type         | Missing values (49)                   | Missing entries                          |
| transaction_category | Valid strings                        | N/A                                      |
| merchant_name        | Missing values (45)                   | Missing entries                          |
| credit_card_number   | Missing and inconsistent string format | Blank entries, some with leading zeros  |

---

## 2. Standardization Strategy

### 2.1 transaction_date
- Standardize all dates to ISO 8601 format: YYYY-MM-DD.
- Use Python library `dateutil.parser` or `pandas.to_datetime` with `errors="coerce"` to parse various formats.
- Example code:
  ```python
  import pandas as pd
  df['transaction_date'] = pd.to_datetime(df['transaction_date'], errors='coerce').dt.strftime('%Y-%m-%d')
  ```
- Handle unparsable dates explicitly by logging or setting to NaT.

### 2.2 currency, account_type, merchant_name
- Impute missing values with the most frequent value (mode) in their respective columns or alternatively drop rows if appropriate.
- Example code for imputation:
  ```python
  for col in ['currency', 'account_type', 'merchant_name']:
      mode_value = df[col].mode()[0]
      df[col].fillna(mode_value, inplace=True)
  ```
- Document the imputation to assess impact on downstream analysis.

### 2.3 credit_card_number
- Convert to string to preserve leading zeros.
- Replace missing/blank values with a placeholder (e.g., 'unknown') or keep as null.
- Example:
  ```python
  df['credit_card_number'] = df['credit_card_number'].astype(str)
  df.loc[df['credit_card_number'].str.strip() == '', 'credit_card_number'] = None
  ```

---

## 3. Validation Post-cleaning
- Verify that all dates conform to YYYY-MM-DD format and no unparsable dates remain.
- Confirm no missing values remain in imputed columns.
- Check data types: transaction_id and account_number as int, amount as float, other text columns as string.
- Sample validation code:
  ```python
  assert df['transaction_date'].str.match(r'^\d{4}-\d{2}-\d{2}$').all()
  assert df['currency'].isnull().sum() == 0
  assert df['account_type'].isnull().sum() == 0
  assert df['merchant_name'].isnull().sum() == 0
  ```

---

## 4. Documentation and Change Tracking
- Maintain a log of all changes and imputations performed.
- Version control scripts and transformation code.
- Record assumptions such as imputing missing values with modes and choice of date format.

---

## 5. Impact Considerations
- Imputation introduces bias that may influence analyses; highlight this in reports.
- Missing credit card numbers may affect fraud detection or customer profiling efforts.

---

## Summary
This standardization approach ensures consistent data types and reliable formats for downstream analytical workflows, improving data quality for the financial dataset.

Please refer to this document as a guide for ongoing data ingestion and cleaning activities.
