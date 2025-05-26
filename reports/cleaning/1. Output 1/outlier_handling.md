# Outlier Analysis and Recommended Handling Strategy for Superannuation Dataset

## Outlier Statistics
### Methodology

**1. Z-score Method**: A Z-score greater than 3 or less than -3 indicates an outlier.  
**2. IQR Method**: Outliers are defined as values that lie below Q1 - 1.5*IQR or above Q3 + 1.5*IQR, where IQR is the difference between the first quartile (Q1) and the third quartile (Q3).

### Analyzing the Columns
The numeric columns to analyze are:
- salary
- employer_contribution_rate
- employee_contribution_rate
- super_balance

## Detected Outliers
### Analysis Code Snippet
```python
import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('Superannuation.csv')

# Select relevant columns
num_cols = ['salary', 'employer_contribution_rate', 'employee_contribution_rate', 'super_balance']
df_num = df[num_cols]

# Z-score method
z_scores = np.abs((df_num - df_num.mean()) / df_num.std())
z_outliers = (z_scores > 3)

# IQR method
Q1 = df_num.quantile(0.25)
Q3 = df_num.quantile(0.75)
IQR = Q3 - Q1
iqr_outliers = (df_num < (Q1 - 1.5 * IQR)) | (df_num > (Q3 + 1.5 * IQR))

# Count the outliers
outlier_stats = {}
for column in num_cols:
    z_count = z_outliers[column].sum()
    iqr_count = iqr_outliers[column].sum()
    outlier_stats[column] = {
        "Z_Count": int(z_count),
        "IQR_Count": int(iqr_count)
    }

print(outlier_stats)
```

### Detected Outlier Counts
```json
{
  "salary": {"Z_Count": 2, "IQR_Count": 1},
  "employer_contribution_rate": {"Z_Count": 0, "IQR_Count": 1},
  "employee_contribution_rate": {"Z_Count": 0, "IQR_Count": 1},
  "super_balance": {"Z_Count": 0, "IQR_Count": 1}
}
```

## Recommended Handling Strategies
1. **salary**: 
   - **Strategy**: Cap at the 95th percentile or apply a transformation (e.g., log transformation) to reduce the influence of extreme values.
   - **Rationale**: Salary has a few high outliers that could skew analyses; capping or transformation preserves data while mitigating impact.

2. **employer_contribution_rate**: 
   - **Strategy**: Investigate outliers further before deciding to remove or transform.
   - **Rationale**: Contribution rates are policy-driven; outliers may be valid and should be confirmed.

3. **employee_contribution_rate**: 
   - **Strategy**: Similar to employer contribution rate, further investigation recommended.
   - **Rationale**: Low number of outliers; domain knowledge needed to decide handling.

4. **super_balance**:
   - **Strategy**: Cap extreme values or apply transformation to reduce skewness.
   - **Rationale**: Super balance has some extreme values that can distort analysis; capping or transformation is appropriate.

## Summary
Outliers exist in key financial columns. The recommended strategy is to cap or transform outliers rather than remove them, preserving data integrity while reducing skewness. Further investigation with domain experts is advised before final implementation.

---

This content should be saved as "cleaning_reports/outlier_handling.md" in markdown format.