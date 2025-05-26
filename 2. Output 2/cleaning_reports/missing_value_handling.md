# Missing Value Analysis and Handling Strategy for Superannuation Dataset

## Missing Value Percentages
| Column Name       | Percentage of Missing Values |
|-------------------|-----------------------------|
| gender            | 10%                         |
| salary            | 15%                         |
| contact_number    | 20%                         |

## Handling Strategies
1. **gender**: 
   - **Imputation Method**: Mode imputation (most common gender).
   - **Rationale**: Low missingness and often recorded as categorical.

2. **salary**: 
   - **Imputation Method**: Median salary imputation based on employment status.
   - **Rationale**: Moderate missingness; median reflects typical salary better than mean in the presence of outliers.

3. **contact_number**: 
   - **Handling Method**: Assess the impact of removing the column or retaining it as is.
   - **Rationale**: High missingness; need to evaluate the criticality of this information depending on analytical needs.
