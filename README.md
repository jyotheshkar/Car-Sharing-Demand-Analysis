# Car-Sharing Demand Database & Data Analytics

## Architecture and maintenance

[Technical architecture, source boundaries, scalability decisions and verification](docs/ARCHITECTURE_MAINTENANCE.md) documents the current implementation and its limits. Maintenance dated 11 November 2026 is separate from the original study or project work.

### Reproducible read-only quick start

```bash
git clone https://github.com/jyotheshkar/Car-Sharing-Demand-Analysis.git
cd Car-Sharing-Demand-Analysis
python scripts/inspect_database.py
python -m unittest discover -s tests -v
```

No external packages are required for the inspection path. Copy an exact table name from the inventory and export with `python scripts/inspect_database.py --table TABLE --output sample.csv --limit 1000`. Output must be a new file. Original notebooks need additional datasets and dependencies; keep the supplied database unchanged.


A comprehensive end-to-end project demonstrating how raw CSV data can be **transformed** into actionable insights using **SQLite database management**, **data preprocessing**, **statistical analysis**, and **machine learning** models (ARIMA, Random Forest, DNN, and clustering).

---

## Table of Contents
1. [Overview](#overview)  
2. [Features](#features)  
3. [Prerequisites](#prerequisites)  
4. [Installation & Setup](#installation--setup)  
5. [Usage](#usage)  
6. [Results & Findings](#results--findings)  
7. [Future Enhancements](#future-enhancements)  
8. [License](#license)

---

## Overview
This project analyzes a **car-sharing dataset** collected hourly from January 2017 to August 2018, focusing on:
- **Database Management:** Building and modifying an SQLite database, categorizing weather and temperature, and creating cohesive reports.  
- **Data Analytics & Preprocessing:** Cleaning, normalizing, and merging essential tables to ensure a high-quality dataset.  
- **Forecasting & Machine Learning:** Employing classical ARIMA, Random Forest, and Deep Neural Networks to predict demand.  
- **Classification & Clustering:** Labeling demand as above/below average and experimenting with multiple clustering algorithms on temperature data.

---

## Features
- **SQLite Integration:** Automated scripts to create backup tables, apply temperature categories (Cold/Mild/Hot), encode weather conditions, and perform advanced SQL queries.  
- **Data Cleaning:** Removal of duplicates, null-value imputation (mean/mode), and normalization for numeric columns.  
- **SQL Insights:** Detailed weekday/weekend (or filtered) demand reports, peak hours, and monthly windspeed/humidity analysis.  
- **Predictive Modeling:**  
  - **ARIMA** for time-series demand forecasting (weekly averages).  
  - **Random Forest** & **DNN** for demand prediction, comparing MSE and RMSE.  
  - **Classification** of demand (above/below average) using Decision Trees, Random Forest, and SVM.  
- **Clustering:** KMeans and Agglomerative clustering on temperature values, testing multiple k-values to identify more uniform clusters.

---

## Prerequisites
- **Python 3.8+**  
- **SQLite**  
- **pip/conda** for managing Python packages  
- Key Python libraries:
  - `pandas`, `numpy`
  - `statsmodels` (time-series analysis)
  - `pmdarima` (for `auto_arima`)
  - `sklearn` (regression, classification, clustering)
  - `tensorflow`/`keras` (for Deep Neural Networks)
  - `matplotlib` or `seaborn` (for data visualization)

---

## Installation & Setup
1. **Clone** the repository:
   ```bash
   git clone https://github.com/jyotheshkar/Car-Sharing-Demand-Analysis.git
   cd Car-Sharing-Demand-Analysis
