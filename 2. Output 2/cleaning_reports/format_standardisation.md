# Format Standardisation Strategy for Superannuation Dataset

## Format Standardisation Issues

| Column Name        | Format Description/Issues                                                                 |
|--------------------|-------------------------------------------------------------------------------------------|
| date_of_birth      | Date stored as string in MM/DD/YYYY format; inconsistent date format possible.             |
| gender             | Categorical values inconsistent (e.g., 'Polygender'); missing values present.               |
| employment_status  | Missing values present; categorical values need standardisation.                          |
| salary             | Missing values present; ensure float type.                                                |
| insurance_coverage | Stored as string 'true'/'false'; should be boolean type.                                  |
| contact_number     | Missing values present; string format may have inconsistencies.                           |

## Standardisation Recommendations

| Column Name        | Recommended Format                                                                         |
|--------------------|-------------------------------------------------------------------------------------------|
| date_of_birth      | Convert to datetime objects in ISO 8601 format (YYYY-MM-DD).                              |
| gender             | Standardise to fixed categories (e.g., 'Male', 'Female', 'Other'); map inconsistent values accordingly. |
| employment_status  | Standardise to fixed categories (e.g., 'employed', 'unemployed', 'self-employed'); map inconsistent values accordingly. |
| salary             | Ensure stored as float; handle missing values separately.                                 |
| insurance_coverage | Convert string 'true'/'false' to boolean True/False.                                     |
| contact_number     | Standardise format to a consistent phone number pattern; keep as string to preserve formatting. |

## Notes

- Missing values handling is addressed separately and not part of this strategy.
- This strategy aims to ensure consistent data formats for reliable analysis and processing.
