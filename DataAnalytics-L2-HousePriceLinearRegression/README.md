# DataAnalytics-L2-HousePriceLinearRegression

**Track:** Data Analytics
**Level:** Level 2 — Task 1
**Task:** Predicting House Prices with Linear Regression

## Objective

Build and evaluate a linear regression model that predicts house prices based on property
features, developing end-to-end skills from data cleaning through to model interpretation.

## Tech Stack

Python, pandas, scikit-learn, matplotlib, seaborn, Jupyter Notebook

## Dataset

`data/Housing.csv` — 545 residential properties with area, bedrooms, bathrooms, stories,
parking, and 7 categorical amenity/location/furnishing fields, with `price` as the target.
Zero missing values.

**Adaptation note:** the task brief names "area, location, number of rooms, and age" as
example predictors. This dataset has no house-age field at all (no substitute used — it's
genuinely absent), and "location" isn't a named column either, so `prefarea` (preferred
neighbourhood, yes/no) is used as the closest available location-quality proxy throughout.

## What's in this folder

```
DataAnalytics-L2-HousePriceLinearRegression/
├── README.md
├── requirements.txt
├── House_Price_Linear_Regression.ipynb   # main notebook, pre-executed with all outputs
├── data/
│   └── Housing.csv
└── screenshots/
    ├── 01_price_distribution.png
    ├── 02_correlation_heatmap.png
    ├── 03_actual_vs_predicted.png
    ├── 04_residual_plot.png
    └── 05_coefficients.png
```

## Feature checklist (all complete, including the bonus)

- [x] EDA: null check, descriptive statistics, target (price) distribution
- [x] Feature selection discussion (markdown, reasoned per feature)
- [x] Missing value handling (confirmed zero present) + One-Hot Encoding of all 7
      categorical columns (`drop_first=True` to avoid the dummy-variable trap)
- [x] Correlation heatmap, with features ranked by correlation strength to price
- [x] Train/test split (80/20)
- [x] Linear Regression trained with scikit-learn
- [x] Evaluation: MSE, RMSE, R²
- [x] Actual vs. predicted scatter plot with a reference diagonal
- [x] Residual plot, checked for systematic pattern
- [x] Coefficient analysis (bar chart + discussion of scale-vs-magnitude nuance)
- [x] **Bonus:** Ridge and Lasso comparison, with features standardised first so the
      regularisation penalty is applied fairly across differently-scaled features

## Results

| Model | MSE | RMSE | R² |
|---|---|---|---|
| Linear Regression | 1,754,318,687,331 | 1,324,507 | **0.6529** |
| Ridge (alpha=1.0, scaled) | 1,754,839,327,447 | 1,324,703 | 0.6528 |
| Lasso (alpha=50000, scaled) | 1,847,224,115,219 | 1,359,126 | 0.6345 |

**Plain Linear Regression performed best**, explaining ~65% of price variance. Ridge and Lasso
don't improve on it here since the correlation heatmap found no severe multicollinearity for
regularisation to correct — but Lasso at a strength high enough to zero out
`furnishingstatus_semi-furnished` demonstrates its built-in feature-selection property at a
small accuracy cost.

**Key finding:** `area`'s raw regression coefficient looks small only because it's measured
in square feet (large-scale units) — this is flagged explicitly in the notebook as a
scale-vs-importance nuance, and is the same reason features are standardised before Ridge/Lasso
(unscaled regularisation would unfairly penalize binary dummy features over `area`).

## How to run

```bash
pip install -r requirements.txt
jupyter notebook
```
Then open `House_Price_Linear_Regression.ipynb` and run all cells
(`Kernel → Restart & Run All`).

## Author

*(Add your full name here before pushing to GitHub / recording your demo video.)*
