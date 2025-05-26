# Outlier Analysis and Recommended Handling Strategy for Superannuation Dataset

## Outlier Statistics
| Column Name                     | Z-Count | IQR Count |
|---------------------------------|---------|-----------|
| salary                          | 2       | 1         |
| employer_contribution_rate      | 0       | 1         |
| employee_contribution_rate      | 0       | 1         |
| super_balance                   | 0       | 1         |

## Recommended Handling Strategies
1. **salary**: 
   - **Strategy**: Cap at the 95th percentile or consider a transformation to reduce the impact of extreme values.
   
2. **employer_contribution_rate**: 
   - **Strategy**: Investigate the cause of the outlier before deciding on removal or treatment.

3. **employee_contribution_rate**: 
   - **Strategy**: Similar to the employer rate; further investigation is needed before imputation or removal.

4. **super_balance**:
   - **Strategy**: Consider capping at a specific threshold to manage extreme values.

Outlier Analysis Dictionary:
{
  "salary": {"Z_Count": 2, "IQR_Count": 1},
  "employer_contribution_rate": {"Z_Count": 0, "IQR_Count": 1},
  "employee_contribution_rate": {"Z_Count": 0, "IQR_Count": 1},
  "super_balance": {"Z_Count": 0, "IQR_Count": 1}
}