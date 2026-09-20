# DataAnalytics-L1-CustomerSegmentation

**Track:** Data Analytics
**Level:** Level 1 — Task 2
**Task:** Customer Segmentation Analysis (RFM + K-Means Clustering)

## Objective

Apply clustering algorithms to segment an e-commerce company's customer base into distinct
groups based on purchasing behaviour, enabling targeted marketing strategies.

## Tech Stack

Python, pandas, scikit-learn (KMeans), matplotlib, seaborn, Jupyter Notebook

## Dataset

`data/OnlineRetail.csv` — the UCI **"Online Retail"** dataset: 541,909 transactions from a
UK-based online gift retailer (01 Dec 2010 – 09 Dec 2011), with InvoiceNo, StockCode,
Description, Quantity, InvoiceDate, UnitPrice, CustomerID, and Country. After removing rows
with no CustomerID and cancelled orders, 397,884 transactions across 4,338 unique customers
remain for the analysis.

## What's in this folder

```
DataAnalytics-L1-CustomerSegmentation/
├── README.md
├── requirements.txt
├── Customer_Segmentation_RFM.ipynb    # main notebook, pre-executed with all outputs
├── data/
│   └── OnlineRetail.csv
└── screenshots/
    ├── 01_elbow_method.png
    ├── 02_cluster_scatterplots.png
    └── 03_customers_per_segment.png
```

## Feature checklist (all complete)

- [x] Load dataset, inspect structure, handle missing values (dropped rows with no
      CustomerID) and inconsistent data (removed cancelled orders and non-positive
      quantity/price rows)
- [x] Descriptive statistics: average order value, purchase frequency, customer lifetime value
- [x] Feature selection: Recency, Frequency, Monetary (RFM) computed per customer
- [x] Data normalisation: log-transform (for skew) + StandardScaler before clustering
- [x] K-Means clustering with the Elbow Method to choose K (K=4 selected)
- [x] Cluster visualisation via 2 scatter-plot feature combinations (Recency×Monetary,
      Frequency×Monetary)
- [x] Cluster profiling: mean R/F/M per cluster with a descriptive customer-type label
- [x] Bar chart: number of customers per cluster
- [x] Insights section with a recommended marketing action per segment

## Segments found

| Segment | Customers | Avg. Recency | Avg. Frequency | Avg. Monetary |
|---|---|---|---|---|
| Champions / VIP | 716 | 12 days | 13.7 orders | £8,074 |
| Loyal / Regular Customers | 1,173 | 71 days | 4.1 orders | £1,803 |
| New / Potential Loyalists | 837 | 18 days | 2.1 orders | £552 |
| Dormant / Lost | 1,612 | 182 days | 1.3 orders | £344 |

**Note on labelling:** segments were named from the actual RFM profile that came out of
clustering rather than forced into a fixed template. In particular, the cluster with low
recency but low frequency/spend was labelled "New / Potential Loyalists" (recent but still
building purchase history) rather than "At-Risk," since a true at-risk profile implies a
*lengthening* gap since last purchase, which is what actually distinguishes the "Loyal /
Regular" cluster here.

## How to run

```bash
pip install -r requirements.txt
jupyter notebook
```
Then open `Customer_Segmentation_RFM.ipynb` and run all cells
(`Kernel → Restart & Run All`).

## Author

*(Add your full name here before pushing to GitHub / recording your demo video.)*
