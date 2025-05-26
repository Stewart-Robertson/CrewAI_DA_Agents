# Exploratory Data Analysis (EDA) on Superannuation Dataset

## Descriptive Statistics for Numerical Columns

### Salary
- Count: 17
- Mean: 156367.45
- Median: 192934.92
- Standard Deviation: 128643.23
- Minimum: 11639.85
- Maximum: 483637.95
- Quartiles: 
  - Q1: 45685.88
  - Q2: 192934.92
  - Q3: 287843.85
- Outliers: Values above 395203.76

### Employer Contribution Rate
- Count: 17
- Mean: 0.1269
- Median: 0.1285
- Standard Deviation: 0.0455
- Minimum: 0.0093
- Maximum: 0.1887
- Quartiles:
  - Q1: 0.0635
  - Q2: 0.1268
  - Q3: 0.1584

### Employee Contribution Rate
- Count: 17
- Mean: 0.0557
- Median: 0.0635
- Standard Deviation: 0.0283
- Minimum: 0.0042
- Maximum: 0.0995
- Quartiles:
  - Q1: 0.0479
  - Q2: 0.0635
  - Q3: 0.0783

### Super Balance
- Count: 17
- Mean: 6080318.75
- Median: 4571745.81
- Standard Deviation: 1225815.57
- Minimum: 127874.46
- Maximum: 9948626.06
- Quartiles:
  - Q1: 306577.44
  - Q2: 4571745.81
  - Q3: 7113751.02

## Frequency Counts for Categorical Columns

### Gender
- Unique Values: 2
- Female: 10 (58.82%)
- Male: 7 (41.17%)
- Missings: 3

### Employment Status
- Unique Values: 3
- Employed: 9 (52.94%)
- Unemployed: 7 (41.18%)
- Self-employed: 3 (17.65%)

### Cities and States
- Summary of distribution/issues mentioned in previous findings.

## Recommendations:
1. Investigate and impute missing values, particularly in salary and gender.
2. Validate categorical entries for consistency and errors.
3. Conduct further analysis on outlier detection for numerical values.