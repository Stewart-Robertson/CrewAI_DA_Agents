import pandas as pd
import numpy as np
from scipy import stats

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def calculate_summary_statistics(df, columns):
    stats_dict = {}
    for col in columns:
        series = df[col].dropna()
        desc = series.describe()
        stats_dict[col] = {
            'count': int(desc['count']),
            'mean': float(desc['mean']),
            'median': float(series.median()),
            'std_dev': float(desc['std']),
            'min': float(desc['min']),
            'max': float(desc['max']),
            'Q1': float(series.quantile(0.25)),
            'Q3': float(series.quantile(0.75))
        }
    return stats_dict

def detect_outliers_iqr(df, column):
    series = df[column].dropna()
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = series[(series < lower_bound) | (series > upper_bound)]
    return outliers, lower_bound, upper_bound

def detect_outliers_zscore(df, column):
    series = df[column].dropna()
    z_scores = np.abs(stats.zscore(series))
    outliers = series[z_scores > 3]
    return outliers

def distribution_analysis(df, numeric_columns):
    distribution_summary = calculate_summary_statistics(df, numeric_columns)
    iqr_outliers = {}
    zscore_outliers = {}
    for col in numeric_columns:
        iqr_outliers[col] = detect_outliers_iqr(df, col)
        zscore_outliers[col] = detect_outliers_zscore(df, col)
    return distribution_summary, iqr_outliers, zscore_outliers

def categorical_counts(df, categorical_columns):
    counts = {}
    for col in categorical_columns:
        counts[col] = df[col].value_counts(dropna=False).to_dict()
    return counts

def generate_markdown_report(stats, iqr_outliers, zscore_outliers, categorical_counts):
    md = []
    md.append("# Exploratory Data Analysis on Superannuation Dataset\n")
    md.append("## Distribution Summary\n")
    md.append("| Column | Count | Mean | Median | Std Dev | Min | Max | Q1 | Q3 |\n")
    md.append("|---|---|---|---|---|---|---|---|---|\n")
    for col, vals in stats.items():
        md.append(f"| {col} | {vals['count']} | {vals['mean']:.2f} | {vals['median']:.2f} | {vals['std_dev']:.2f} | {vals['min']:.2f} | {vals['max']:.2f} | {vals['Q1']:.2f} | {vals['Q3']:.2f} |\n")
    md.append("\n## Outlier Analysis\n")
    md.append("### IQR Method Outliers\n")
    for col, (outliers, lower_bound, upper_bound) in iqr_outliers.items():
        if not outliers.empty:
            md.append(f"- **{col}**: Outliers detected outside the range [{lower_bound:.2f}, {upper_bound:.2f}]. Values: {list(outliers.values)}\n")
        else:
            md.append(f"- **{col}**: No outliers detected.\n")
    md.append("\n### Z-Score Method Outliers\n")
    for col, outliers in zscore_outliers.items():
        if not outliers.empty:
            md.append(f"- **{col}**: Outliers detected with Z-score > 3. Values: {list(outliers.values)}\n")
        else:
            md.append(f"- **{col}**: No outliers detected.\n")
    md.append("\n## Categorical Variables Summary\n")
    for col, counts in categorical_counts.items():
        md.append(f"### {col}\n")
        md.append("| Category | Count |\n")
        md.append("|---|---|\n")
        for category, count in counts.items():
            md.append(f"| {category} | {count} |\n")
        md.append("\n")
    md.append("## Recommendations\n1. Investigate anomalies and outliers especially in salary and super balance for data quality issues.\n2. Consider imputation or removal strategies for missing salary data.\n3. Explore relationships between numerical and categorical variables for better insights.\n")
    md.append("\n## Conclusion\nThis exploratory data analysis reveals the distributional properties and outlier presence in key superannuation financial variables, providing a foundation for deeper analysis and data quality improvement.")
    return "\n".join(md)

if __name__ == '__main__':
    data_path = 'temp_superannuation_data.csv'
    df = load_data(data_path)
    numeric_cols = ['salary', 'employer_contribution_rate', 'employee_contribution_rate', 'super_balance']
    cat_cols = ['gender', 'employment_status', 'investment_option', 'insurance_coverage']

    dist_summary, iqr_outliers, zscore_outliers = distribution_analysis(df, numeric_cols)
    cat_counts = categorical_counts(df, cat_cols)

    report_md = generate_markdown_report(dist_summary, iqr_outliers, zscore_outliers, cat_counts)

    with open('eda_reports/eda_distribution.md', 'w') as f:
        f.write(report_md)
