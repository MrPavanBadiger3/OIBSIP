# Retail Sales — Data Analytics Rack

This repo holds the completed tasks for the **Data Analytics** rack. Each task lives in its
own notebook under `notebooks/`, with its dataset under `data/`.

## Project structure

```
retail-sales-eda/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   └── retail_sales_dataset.csv      # Task 1 dataset
└── notebooks/
    └── EDA_Retail_Sales.ipynb        # Task 1: EDA on Retail Sales Data
```

As later tasks (e.g. Task 2 — Customer Segmentation) are completed, their notebooks and
datasets will be added alongside these in the same `notebooks/` and `data/` folders.

## Task 1 — EDA on Retail Sales Data

**Dataset:** 1,000 retail transactions (Jan 2023 – Jan 2024) with Transaction ID, Date,
Customer ID, Gender, Age, Product Category, Quantity, Price per Unit, and Total Amount.

**What the notebook covers:**
- Initial inspection (shape, dtypes, nulls, duplicates)
- Descriptive statistics
- Monthly and quarterly sales trend charts
- Customer demographics (age distribution, gender breakdown)
- Revenue by product category, top-10 customers by spend
- Correlation heatmap
- A non-obvious insight: average order value by age group × gender
- Markdown commentary after every chart
- A conclusion with 3 actionable business recommendations

## Local setup

1. **Install Python 3.10+** if you don't already have it — [python.org/downloads](https://www.python.org/downloads/).
2. **Clone or download this folder**, then open a terminal inside it.
3. **Create and activate a virtual environment:**

   macOS / Linux:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   Windows (PowerShell):
   ```powershell
   python -m venv venv
   venv\Scripts\Activate.ps1
   ```

4. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Launch Jupyter:**
   ```bash
   jupyter notebook
   ```
   This opens a browser tab. Navigate into `notebooks/` and open `EDA_Retail_Sales.ipynb`.
6. **Run the notebook:** use the menu `Kernel → Restart & Run All`, or click through cells
   with `Shift + Enter`. The notebook reads its data via a relative path
   (`../data/retail_sales_dataset.csv`), so keep the folder structure intact — don't move the
   notebook out of `notebooks/` on its own.

### Alternative: VS Code

If you use VS Code instead of the browser Jupyter UI, install the **Python** and **Jupyter**
extensions, open this folder, then open the `.ipynb` file directly and run cells from there —
same virtual environment and `requirements.txt` apply.

## Notes

- The dataset tracks sales at the *product-category* level (Beauty, Clothing, Electronics),
  not by individual product name/SKU. Where the task brief calls for a "top 10 best-selling
  products" chart, the notebook substitutes the closest meaningful equivalent (top-10
  customers by spend + category-level revenue ranking) and explains this adaptation inline.
