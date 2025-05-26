# Data Type Standardisation Strategy for Superannuation Dataset

## Issues Identified

| Column Name               | Issue Description                                                                                  |
|---------------------------|--------------------------------------------------------------------------------------------------|
| date_of_birth             | Date stored as string in MM/DD/YYYY format; inconsistent date format possible.                    |
| gender                    | Categorical values inconsistent (e.g., 'Polygender'); missing values present.                      |
| employment_status         | Missing values present; categorical values need standardisation.                                 |
| salary                    | Missing values present; ensure float type.                                                       |
| insurance_coverage        | Stored as string "true"/"false"; should be boolean type.                                     |
| contact_number            | Missing values present; string format may have inconsistencies.                                 |

## Type Conversions

| Column Name               | Recommended Data Type                                                                             |
|---------------------------|--------------------------------------------------------------------------------------------------|
| member_id                 | Integer                                                                                          |
| first_name                | String                                                                                           |
| last_name                 | String                                                                                           |
| date_of_birth             | DateTime (ISO 8601 format)                                                                       |
| gender                    | Categorical String (standardised categories)                                                    |
| employment_status         | Categorical String (standardised categories)                                                    |
| salary                    | Float                                                                                           |
| employer_contribution_rate| Float                                                                                           |
| employee_contribution_rate| Float                                                                                           |
| super_balance             | Float                                                                                           |
| investment_option         | String                                                                                           |
| insurance_coverage        | Boolean                                                                                         |
| beneficiary_name          | String                                                                                           |
| beneficiary_relationship  | String                                                                                           |
| contact_number            | String                                                                                           |
| email                     | String                                                                                           |
| address                   | String                                                                                           |
| city                      | String                                                                                           |
| state                     | String                                                                                           |
| postal_code               | String                                                                                           |

## Standardisation Strategy

- Convert `date_of_birth` strings to datetime objects in ISO 8601 format for consistency.
- Standardise categorical columns `gender` and `employment_status` by defining a fixed set of categories and mapping existing values accordingly.
- Convert `insurance_coverage` from string to boolean type.
- Ensure numeric columns (`salary`, `employer_contribution_rate`, `employee_contribution_rate`, `super_balance`) are stored as floats.
- Keep `contact_number` and `postal_code` as strings to preserve formatting and leading zeros.
- Handle missing values separately as per missing value handling strategy; not part of this task.

This strategy ensures consistent data types across the dataset, facilitating reliable analysis and processing.
