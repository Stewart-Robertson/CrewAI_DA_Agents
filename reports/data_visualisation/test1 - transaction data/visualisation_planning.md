# Visualisation Planning for Original Dataset

## Visualisation Types and Justifications

| Column Name          | Data Type  | Proposed Visualisation Type      | Justification |
|----------------------|------------|---------------------------------|---------------|
| transaction_id       | Numerical  | Histogram                       | To show distribution and ensure uniqueness and no duplicates over the ID range.
| transaction_date     | Date/String| Time Series Line Chart          | To observe transaction trends over time (requires date parsing and standardisation).
| amount              | Numerical  | Histogram + Box Plot            | Histogram to show value distribution and Box Plot to highlight outliers and spread.
| currency            | Categorical| Bar Chart                      | To depict frequency of each currency, handles up to 15 unique values well.
| transaction_type    | Categorical| Bar Chart / Pie Chart          | Bar chart for clear count comparison, pie chart could show proportion of each type.
| account_number      | Numerical  | Histogram                      | To detect patterns or anomalies in account numbers; maybe limited insight due to IDs.
| account_type        | Categorical| Bar Chart                      | To show distribution across account types; 3 unique categories, easy to compare.
| transaction_category| Categorical| Bar Chart                      | To display count by each category, simple and informative.
| merchant_name       | Categorical| Bar Chart with Top N + Others  | With 300 unique merchants, plot top 10 or 15 and aggregate rest as 'Others' to reduce clutter.
| credit_card_number  | Numerical  | Histogram                      | Primarily an identifier; histogram can reveal any unusual distribution patterns.

## Notes and Best Practices

- Use accessible color palettes (e.g., ColorBrewer) ensuring color differentiation for categorical variables.
- Include clear axis labels and legends.
- Handle missing values by indicating as separate category or excluding as appropriate.
- For large cardinality columns like merchant_name, reduce complexity by grouping less frequent categories.

## Summary Dictionary

```python
visualisation_plan = {
    'transaction_id': 'Histogram',
    'transaction_date': 'Time Series Line Chart',
    'amount': 'Histogram + Box Plot',
    'currency': 'Bar Chart',
    'transaction_type': 'Bar Chart / Pie Chart',
    'account_number': 'Histogram',
    'account_type': 'Bar Chart',
    'transaction_category': 'Bar Chart',
    'merchant_name': 'Bar Chart (Top N with Others)',
    'credit_card_number': 'Histogram'
}
```

This plan aligns with the characteristics of the dataset as revealed in the EDA, and aims to provide clear, accessible, and informative visual summaries to support further analysis and reporting.