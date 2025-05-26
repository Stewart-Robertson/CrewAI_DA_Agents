# Format Standardisation Strategy for Superannuation Dataset

## Format Standardisation Issues Identified

| Column Name           | Format Description / Issues                                                                                 |
|-----------------------|------------------------------------------------------------------------------------------------------------|
| date_of_birth         | Stored as string in MM/DD/YYYY format; inconsistent or invalid dates possible; needs conversion to ISO 8601 (YYYY-MM-DD).
| gender                | String with inconsistent values including missing, different capitalizations, and non-binary categories (e.g., Polygender, Bigender).
| employment_status     | String with missing values and inconsistent categories.
| insurance_coverage    | Stored as string "true"/"false"; should be boolean True/False.
| contact_number        | String with missing values and inconsistent formatting (dashes, spaces); needs standardisation.
| postal_code           | String with inconsistent formats (spaces, letters, numbers); needs trimming and standardisation.
| state                 | Contains missing values and inconsistent abbreviations; needs standardisation.

## Standardisation Recommendations

| Column Name           | Recommended Format / Standardisation Strategy                                                               |
|-----------------------|------------------------------------------------------------------------------------------------------------|
| date_of_birth         | Convert to datetime type with ISO 8601 format (YYYY-MM-DD).
| gender                | Standardise categories to ["Male", "Female", "Other", "Unknown"]; map non-binary to "Other" and missing to "Unknown"; consistent capitalization.
| employment_status     | Standardise categories to ["employed", "unemployed", "self-employed", "unknown"] all lowercase; map missing to "unknown".
| insurance_coverage    | Convert from string "true"/"false" to boolean True/False.
| contact_number        | Remove all non-numeric characters; standardise to digits only format; keep missing as is.
| postal_code           | Trim spaces, uppercase letters; standardise format depending on country if known; otherwise keep consistent.
| state                 | Standardise to uppercase abbreviations; fill missing with "Unknown".

## Summary

This strategy addresses the key format inconsistencies identified in the Superannuation dataset. Implementing these standardisations will improve data consistency, facilitate analysis, and support further data cleaning and validation steps.

## Notes

- Missing values are acknowledged but not handled here as per task instructions.
- Assumptions include mapping non-binary gender categories to "Other" and missing to "Unknown".
- Contact number formatting assumes digits-only standardisation.

## Example Code Snippets

```python
import pandas as pd

# Load dataset
# df = pd.read_csv('Superannuation.csv')

# Convert date_of_birth to datetime
# df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], format='%m/%d/%Y', errors='coerce').dt.strftime('%Y-%m-%d')

# Standardise gender
# gender_map = {'Male': 'Male', 'Female': 'Female', 'Polygender': 'Other', 'Bigender': 'Other', None: 'Unknown'}
# df['gender'] = df['gender'].str.capitalize().map(gender_map).fillna('Unknown')

# Standardise employment_status
# employment_status_map = {'employed': 'employed', 'unemployed': 'unemployed', 'self-employed': 'self-employed', None: 'unknown'}
# df['employment_status'] = df['employment_status'].str.lower().map(employment_status_map).fillna('unknown')

# Convert insurance_coverage to boolean
# df['insurance_coverage'] = df['insurance_coverage'].map({'true': True, 'false': False})

# Standardise contact_number
# df['contact_number'] = df['contact_number'].str.replace(r'\D', '', regex=True)

# Standardise postal_code
# df['postal_code'] = df['postal_code'].str.strip().str.upper()

# Standardise state
# df['state'] = df['state'].str.upper().fillna('Unknown')
```