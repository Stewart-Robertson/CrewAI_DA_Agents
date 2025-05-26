# Visualisation Planning for Superannuation Dataset

## Introduction
This document outlines the planned visualisations for the Superannuation dataset based on the exploratory data analysis findings and dataset characteristics.

## Visualisation Types and Justifications

| Column Name             | Visualisation Type(s)          | Justification |
|------------------------|------------------------------|---------------|
| member_id              | None                         | Unique identifier, not suitable for visualisation. |
| first_name, last_name  | None                         | Identifiers, no analytical value for visualisation. |
| date_of_birth          | Histogram, Boxplot            | To show age distribution (after conversion), detect outliers, and understand demographics. |
| gender                 | Bar Chart, Pie Chart          | Categorical with few categories; bar and pie charts show distribution and proportions. |
| employment_status      | Bar Chart, Pie Chart          | Categorical; visualise employment distribution. |
| salary                 | Histogram, Boxplot, Violin Plot | Numerical with outliers; histograms show distribution, boxplots highlight outliers, violin plots show distribution shape. |
| employer_contribution_rate | Histogram, Boxplot        | Numerical; understand distribution and detect outliers. |
| employee_contribution_rate | Histogram, Boxplot        | Numerical; understand distribution and detect outliers. |
| super_balance          | Histogram, Boxplot, Violin Plot | Numerical with outliers; similar rationale as salary. |
| investment_option      | Bar Chart, Pie Chart          | Categorical with multiple categories; bar and pie charts show distribution. |
| insurance_coverage     | Bar Chart, Pie Chart          | Boolean categorical; bar and pie charts show proportions. |
| beneficiary_name       | None                         | Identifier, not suitable for visualisation. |
| beneficiary_relationship | Bar Chart, Pie Chart        | Categorical; visualise distribution of relationships. |
| contact_number         | None                         | Contact info, not suitable for visualisation. |
| email                  | None                         | Identifier, not suitable for visualisation. |
| address, city, state, postal_code | Bar Chart (for city, state) | Geographic categorical data; bar charts show frequency distribution. |

## Summary
- Histograms and boxplots are chosen for numerical columns to understand distributions and detect outliers.
- Violin plots provide detailed distribution shapes for salary and super_balance due to outliers.
- Bar and pie charts are selected for categorical variables to show counts and proportions.
- Identifiers and sensitive personal information are excluded from visualisation.
- Geographic data visualised with bar charts; advanced maps could be considered later.

## Visualisation Types Dictionary

```python
visualisation_types = {
    "date_of_birth": ["Histogram", "Boxplot"],
    "gender": ["Bar Chart", "Pie Chart"],
    "employment_status": ["Bar Chart", "Pie Chart"],
    "salary": ["Histogram", "Boxplot", "Violin Plot"],
    "employer_contribution_rate": ["Histogram", "Boxplot"],
    "employee_contribution_rate": ["Histogram", "Boxplot"],
    "super_balance": ["Histogram", "Boxplot", "Violin Plot"],
    "investment_option": ["Bar Chart", "Pie Chart"],
    "insurance_coverage": ["Bar Chart", "Pie Chart"],
    "beneficiary_relationship": ["Bar Chart", "Pie Chart"],
    "city": ["Bar Chart"],
    "state": ["Bar Chart"]
}
```

## Justifications Dictionary

```python
justifications = {
    "date_of_birth": "Histogram and boxplot to understand age distribution and detect outliers after converting to age.",
    "gender": "Bar and pie charts effectively show the distribution and proportions of categorical gender data.",
    "employment_status": "Bar and pie charts to visualize employment categories and their proportions.",
    "salary": "Histogram, boxplot, and violin plot to explore distribution, detect outliers, and understand data shape.",
    "employer_contribution_rate": "Histogram and boxplot to analyze distribution and identify outliers.",
    "employee_contribution_rate": "Histogram and boxplot for distribution and outlier detection.",
    "super_balance": "Histogram, boxplot, and violin plot to explore distribution and outliers in super balance.",
    "investment_option": "Bar and pie charts to show distribution of investment choices.",
    "insurance_coverage": "Bar and pie charts to show proportions of boolean insurance coverage.",
    "beneficiary_relationship": "Bar and pie charts to visualize distribution of beneficiary relationships.",
    "city": "Bar chart to show frequency distribution of members by city.",
    "state": "Bar chart to show frequency distribution of members by state."
}
```
