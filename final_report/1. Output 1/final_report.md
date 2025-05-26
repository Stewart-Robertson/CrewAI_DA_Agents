# Final Report on Superannuation Dataset Analysis

## 1. Data Cleaning Summary

The Superannuation dataset contains 49 rows and 20 columns with personal and financial information. Key data cleaning actions included:

- Handling missing values in `gender`, `salary`, and `contact_number` columns using mode and median imputation strategies.
- Standardising data types: converting `date_of_birth` to ISO 8601 date format, `insurance_coverage` to boolean, and standardising categorical columns like `gender` and `employment_status`.
- Formatting standardisation for contact numbers, postal codes, and state abbreviations.
- Duplicate analysis found no exact duplicates based on `member_id`; manual verification recommended for potential duplicates based on personal identifiers.
- Outlier analysis identified outliers in `salary` and `super_balance`; recommended capping or transformation to mitigate skewness.

## 2. Exploratory Data Analysis Summary

### Data Overview
- Total Rows: 49
- Total Columns: 20

### Numerical Variables Summary
| Column | Count | Mean | Median | Std Dev | Min | Max |
|---|---|---|---|---|---|---|
| Salary | 43 | 239,866.82 | 280,324.4 | 106,160.14 | 11,639.85 | 483,637.95 |
| Employer Contribution Rate | 49 | 0.1163 | 0.1439 | 0.0440 | 0.0052 | 0.1974 |
| Employee Contribution Rate | 49 | 0.0588 | 0.0598 | 0.0251 | 0.0012 | 0.0995 |
| Super Balance | 49 | 6,583,978.4 | 8,680,505 | 1,874,015.7 | 127,874.46 | 9,927,973.22 |

### Categorical Variables Summary
- Gender: Male (19), Female (25), Polygender (1), Bigender (2)
- Employment Status: Employed (20), Unemployed (20), Self-employed (8)
- Investment Options: Growth (9), Moderate (12), Conservative (8), Balanced (12), High Growth (12), Cash (4)
- Insurance Coverage: True (29), False (20)

### Key Findings
- Moderate positive correlation between salary and super balance (0.356), and salary and employer contribution rate (0.387).
- Employee contribution rate showed weak correlation with other variables.
- Missing salary values (6 entries) require imputation for accurate analysis.
- Diverse gender representation including non-binary categories.

## 3. Visualisation Summary

The following visualisations were created to support analysis:

- Date of Birth: Histogram and Boxplot showing age distribution and outliers.
- Gender: Bar Chart and Pie Chart illustrating gender distribution.
- Employment Status: Bar Chart and Pie Chart showing employment categories.
- Salary: Histogram, Boxplot, and Violin Plot highlighting distribution and outliers.
- Employer and Employee Contribution Rates: Histograms and Boxplots.
- Super Balance: Histogram, Boxplot, and Violin Plot.
- Investment Option: Bar Chart and Pie Chart.
- Insurance Coverage: Bar Chart and Pie Chart.
- Beneficiary Relationship: Bar Chart and Pie Chart.
- City and State: Bar Charts showing geographic distribution.

### Visualisation Files
- visualisation_reports/date_of_birth_histogram.png
- visualisation_reports/date_of_birth_boxplot.png
- visualisation_reports/gender_bar_chart.png
- visualisation_reports/gender_pie_chart.png
- visualisation_reports/employment_status_bar_chart.png
- visualisation_reports/employment_status_pie_chart.png
- visualisation_reports/salary_histogram.png
- visualisation_reports/salary_boxplot.png
- visualisation_reports/salary_violin_plot.png
- visualisation_reports/employer_contribution_rate_histogram.png
- visualisation_reports/employer_contribution_rate_boxplot.png
- visualisation_reports/employee_contribution_rate_histogram.png
- visualisation_reports/employee_contribution_rate_boxplot.png
- visualisation_reports/super_balance_histogram.png
- visualisation_reports/super_balance_boxplot.png
- visualisation_reports/super_balance_violin_plot.png
- visualisation_reports/investment_option_bar_chart.png
- visualisation_reports/investment_option_pie_chart.png
- visualisation_reports/insurance_coverage_bar_chart.png
- visualisation_reports/insurance_coverage_pie_chart.png
- visualisation_reports/beneficiary_relationship_bar_chart.png
- visualisation_reports/beneficiary_relationship_pie_chart.png
- visualisation_reports/city_bar_chart.png
- visualisation_reports/state_bar_chart.png

## 4. Critical Evaluation of Findings

- The dataset is relatively small (49 rows), which limits the statistical power of analyses.
- Missing values in key columns like salary and gender require careful imputation to avoid bias.
- Outliers in salary and super balance may skew results; capping or transformation is advisable.
- The presence of non-binary gender categories suggests inclusivity but may require tailored analysis approaches.
- Correlations indicate salary and employer contributions are linked, but employee contributions show weak relationships, suggesting potential for member education.
- Geographic distribution visualisations can inform regional targeting of services.

## 5. Actionable Recommendations

- Implement imputation strategies for missing salary and gender values as per cleaning strategy.
- Apply capping or log transformation to salary and super balance to reduce skewness.
- Educate members on employee contributions to enhance super balance growth.
- Conduct manual review for potential duplicates based on personal identifiers.
- Use geographic insights to tailor member engagement and services.
- Monitor data quality continuously to maintain dataset integrity.

## 6. Possibilities for Further Analysis or Process Improvements

- Perform time-based analysis by deriving age from date_of_birth and examining trends.
- Explore the impact of investment options on super balance growth.
- Analyze insurance coverage uptake and its correlation with demographics.
- Investigate reasons behind missing contact numbers and improve data collection.
- Develop predictive models for super balance based on demographic and financial variables.
- Enhance data validation processes to prevent duplicates and inconsistencies.

---

*This report consolidates data cleaning, exploratory analysis, and visualisation insights to support informed decision-making and continuous improvement in managing the Superannuation dataset.*
