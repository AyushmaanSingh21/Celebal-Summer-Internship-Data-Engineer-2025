# 🚕 Week 8 – NYC Yellow Taxi Data Analytics using PySpark

This project is based on analyzing real-world taxi trip data from NYC using **PySpark** inside a **Jupyter Notebook**. The goal is to load, transform, and extract insights from the dataset through DataFrame-based operations.

## 📓 [Notebook](./week8.ipynb)

## 📁 Dataset Information

- **Source:** [NYC Taxi & Limousine Commission - Kaggle](https://www.kaggle.com/datasets/gauravpathak1789/yellow-tripdata-2020-01)
- **Filename:** `yellow_tripdata_2020-01.csv`
- **Size:** ~295 MB+
- Includes columns for fare details, trip times, pickup/drop locations, tips, surcharges, etc.

> 📌 You can also find original data from the official [TLC site](https://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml)

---

## ⚙️ Tools & Tech Used

- Python
- PySpark (Apache Spark 3.x)
- Jupyter Notebook
- Parquet format for storage optimization

---

## 🔄 Workflow Steps

1. Loaded the `.csv` file into a Spark DataFrame
2. Cleaned and preprocessed the data:
   - Converted string timestamps to proper datetime format
   - Casted relevant fields to numeric types
3. Wrote the cleaned data as a Parquet file to optimize querying
4. Ran a series of analytical queries on the processed data

---

## 🔍 Analytical Queries Performed

| Query | Summary |
|-------|---------|
| **Q1** | Created a `Revenue` column by summing up 'Fare_amount', 'Extra', 'MTA_tax', 'Improvement_surcharge', 'Tip_amount', 'Tolls_amount', and 'Total_amount' |
| **Q2** | Counted total passengers grouped by pickup location area |
| **Q3** | Calculated average fare and total earnings for both vendors |
| **Q4** | Computed a rolling count of payments for each payment type |
| **Q5** | Identified the top 2 highest earning vendors on a specific day, showing total distance and passenger count |
| **Q6** | Found the most traveled route based on maximum passenger count between pickup and dropoff |
| **Q7** | Fetched top pickup locations with the most passengers in the last simulated 5–10 seconds |

---

