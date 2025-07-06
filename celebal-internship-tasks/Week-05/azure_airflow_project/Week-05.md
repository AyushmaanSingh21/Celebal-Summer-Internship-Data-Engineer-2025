<h1 align="center">Week 5 Assignment: Data Integration & Pipeline Automation</h1>

> **Thanks to [CSI (Celebal Summer Internship)](https://www.celebaltech.com/)** for this amazing learning opportunity.  
>
> This task gave me real-world experience with data engineering tools, storage services, and ETL pipeline development!

<p align="center">
  <img src="./images/flowchart.png" alt="ETL Pipeline Diagram" width="600"/>
</p>

---

## 🚀 Overview

In this project, I built a mini **ETL pipeline** that:
- Extracts data from a **local SQLite database**
- Converts it into multiple formats: **CSV**, **Parquet**, and **Avro**
- Uploads the data to **Azure Blob Storage** in a structured format
- Contains a production-ready **Airflow DAG** (not executed due to Windows OS limitations)

This pipeline simulates real-world use cases like:
- Data warehousing
- Format interoperability
- Cloud storage
- Scheduled automation

---

## 🛠️ Technologies Used

| Tool             | Purpose                                     |
|------------------|---------------------------------------------|
| **SQLite (via VS Code)** | Lightweight local database (easy setup)     |
| **Python + Pandas**   | Read/write SQL data, format export           |
| **PyArrow & FastAvro** | Efficient serialization (Parquet/Avro)       |
| **Azure Blob Storage** | Cloud-based object storage for tables/files |
| **Apache Airflow**     | (Optional) DAG orchestration engine         |

---

## 📌 Why I Chose SQLite over AWS RDS

- It's easier to set up and test locally in VS Code
- No internet dependency or AWS billing
- Still realistic for prototyping and proof-of-concept pipelines

---

## ⚠️ About Airflow Limitation

I wrote a **working DAG (`db_to_azure_dag.py`)** for Airflow, but **could not run it on my local system** due to Windows OS limitations (missing `os.register_at_fork` error).  
This is a common known issue.

✅ Still, the DAG is **ready for production**, and I’ve explained how it works in the comments.  
If needed, I’m happy to walk through it or even record a 20-second video as suggested in the internship docs.

---

## 🧪 Project Steps (Simplified)

1️⃣ **Prepare your DB**  
Using SQLite (`sample.db`) with a `products` table:
```sql
CREATE TABLE products (
    id INTEGER,
    name TEXT,
    price REAL,
    quantity INTEGER
);
