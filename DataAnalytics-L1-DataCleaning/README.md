# DataAnalytics-L1-DataCleaning

**Track:** Data Analytics
**Level:** Level 1 — Task 3
**Task:** Cleaning Data

## Objective

Demonstrate professional-level data cleaning skills by taking a deliberately messy dataset
and systematically transforming it into a clean, analysis-ready dataset, documenting every
decision.

## Tech Stack

Python, pandas, numpy, Jupyter Notebook

## Dataset

`data/healthcare_dataset_messy.csv` — 203 patient admission records across 14 columns,
deliberately constructed with realistic data-quality problems: missing values, duplicate
rows, patient-ID collisions, inconsistent categorical formatting, mixed date formats,
impossible sentinel values, and inconsistent text casing.

## What's in this folder

```
DataAnalytics-L1-DataCleaning/
├── README.md
├── requirements.txt
├── Data_Cleaning_Healthcare.ipynb          # main notebook, pre-executed with all outputs
└── data/
    ├── healthcare_dataset_messy.csv        # original messy input
    └── healthcare_dataset_cleaned.csv       # cleaned output (produced by the notebook)
```

## Feature checklist (all complete)

- [x] Data quality report: nulls per column, duplicate rows, data type issues, value range
      anomalies
- [x] Missing data handling: a strategy chosen and justified per column (median, mode,
      constant placeholder, or row deletion — see table below)
- [x] Duplicate removal: exact duplicates, same-patient re-entries, and genuine ID collisions
      each handled differently and documented
- [x] Standardisation: gender/department/status/insurance casing unified, phone numbers
      reformatted, names and emails normalised, 4+ date formats parsed into one datetime type
- [x] Outlier detection: IQR method used on `age` and `billing_amount`; impossible sentinel
      values (`-1`, `999`) treated as missing rather than capped
- [x] Data type correction: `patient_id` as string, `billing_amount` as float, `admit_date`
      as datetime
- [x] Before vs. after summary table: row count, null count, duplicate count, dtype accuracy
- [x] Cleaned dataset saved to a new CSV file

## Key cleaning decisions

| Issue | Strategy | Why |
|---|---|---|
| 3 exact duplicate rows | Dropped | Zero information loss |
| 4 patient-ID collisions between *different* patients | Reassigned a new ID to the second record | Deleting either would destroy a real patient's only record |
| `age` = `-1` or `999` | Treated as missing, then median-imputed | Physically impossible sentinel values, not genuine extremes |
| `age`, `billing_amount` nulls | Median imputation | Numeric, right-skewed — more robust than mean |
| `gender`, `status` nulls | Mode imputation | Reasonable default for demographic/operational fields |
| `department`, `diagnosis`, `attending_doctor`, `insurance_provider`, `email` nulls | Constant placeholder (`"Unknown"`, `"Not Recorded"`, etc.) | Guessing a specific diagnosis or doctor for a real patient would fabricate clinical facts |
| 3 rows missing 4+ fields | Row deletion | Too sparse to be a reliable record |
| Forward fill | **Not used anywhere** | Each row is an independent patient admission, not a time series — forward-filling would leak one patient's data onto another's record |

## Result

| Metric | Before | After |
|---|---|---|
| Row count | 203 | 197 |
| Total null values | 207 | 0 |
| Duplicate rows | 3 | 0 |
| Correct dtypes (key columns) | 1/8 | 8/8 |

## How to run

```bash
pip install -r requirements.txt
jupyter notebook
```
Then open `Data_Cleaning_Healthcare.ipynb` and run all cells
(`Kernel → Restart & Run All`). The cleaned CSV is written to `data/healthcare_dataset_cleaned.csv`.

## Author

*(Add your full name here before pushing to GitHub / recording your demo video.)*
