# Missing Value Analysis Report for Superannuation Dataset

## Missing Values Analysis

### Columns with Missing Values:
- **gender:** Missing for rows 6 and 7
- **salary:** Missing for rows 5, 6, and 16
- **contact_number:** Missing for rows 5, 8, 17, and 19

### Count of Missing Values:
- **gender:** 2 missing values
- **salary:** 3 missing values
- **contact_number:** 4 missing values

## Strategy for Handling Missing Values

1. **gender:**
   - **Strategy:** Imputation using the mode of the column.

2. **salary:**
   - **Strategy:** Imputation using the median of the salary column.

3. **contact_number:**
   - **Strategy:**
     - Attempting to retrieve the missing values from other sources if available.
     - If not possible, we could impute with a placeholder value indicating missing data (e.g., "N/A") or leave them as is if no other information is available.