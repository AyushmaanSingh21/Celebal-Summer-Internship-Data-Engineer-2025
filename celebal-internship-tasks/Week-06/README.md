
# Week 6: Azure Data Factory ETL Project

In this task, we build an **ETL pipeline using Azure Data Factory (ADF)** that extracts data from:

* A **Blob CSV file (Netflix dataset)** uploaded to Azure Storage
* The data is then loaded into an **Azure SQL Database**

We also discuss **incremental load logic**, and optionally how to schedule the pipeline using triggers.

> **Thanks to [CSI (Celebal Summer Internship)](https://www.celebaltech.com/)**  
> This task gave me a deep understanding of building ETL pipelines in ADF using its no-code, drag-and-drop interface.  
> I'm grateful for the opportunity to learn and build!

---

## 🪜 Steps Followed

1. **Created Azure SQL Database** from portal
2. **Enabled public access and allowed Azure services**
3. **Created table manually** in SQL using Query Editor or SSMS
4. **Uploaded Netflix CSV dataset** to Azure Blob Storage
5. Opened **Azure Data Factory Studio**
6. Created two **Linked Services**:
   - One to **Blob Storage**
   - One to **Azure SQL DB**
7. Created **datasets** for:
   - Netflix CSV (source)
   - SQL Table (sink)
8. Created **Copy Activity pipeline** to move data from Blob to SQL
9. **Debugged pipeline** to verify correctness
10. **Published pipeline** to finalize it

---

## 🖼️ Screenshot Gallery

| Screenshot | Description |
|------------|-------------|
| `pipeline_overview.png` | Overall view of ADF pipeline with Copy Activity |
| `linked_service_blob.png` | Linked Service configuration for Blob Storage |
| `linked_service_sql.png` | Linked Service configuration for Azure SQL |
| `dataset_blob_csv.png` | Dataset config for Netflix CSV file |
| `dataset_sql_sink.png` | Dataset config for SQL sink table |
| `copy_activity.png` | Copy activity showing Source and Sink |
| `debug_success.png` | Successful debug output showing data copied |
| `adf_publish.png` | Publish confirmation screenshot in ADF |

---

### 🧩 ADF Pipeline Overview

<p align="center">
  <img src="./images/pipeline_overview.png" alt="ADF Pipeline Overview" width="600"/>
</p>

---

### 🔗 Linked Services

**Blob Storage**
<p align="center">
  <img src="./images/blob_linked_service.png" alt="Blob Storage Linked Service" width="600"/>
</p>

**Azure SQL Database**
<p align="center">
  <img src="./images/sql_linked_service.png" alt="Azure SQL Linked Service" width="600"/>
</p>

---

### 📊 Datasets

<p align="center">
  <img src="./images/dataset_blob.png" alt="Blob Dataset" width="600"/>
</p>

<p align="center">
  <img src="./images/dataset_sql.png" alt="SQL Dataset" width="600"/>
</p>

---

### 🔁 Copy Activity

<p align="center">
  <img src="./images/copy_activity.png" alt="Copy Activity" width="600"/>
</p>

---

### 🧪 Debug Result

<p align="center">
  <img src="./images/pipeline_debug_success.png" alt="Debug Success" width="600"/>
</p>

---

### 🗂️ SQL Table Data Preview

<p align="center">
  <img src="./images/sql_data_preview.png" alt="SQL Table Preview" width="600"/>
</p>

---

### ⏰ Trigger Setup (Optional)

<p align="center">
  <img src="./images/trigger_setup.png" alt="Monthly Trigger Setup" width="600"/>
</p>

---


## ✅ Summary

| Task                     | Status |
|--------------------------|--------|
| Blob → SQL Pipeline      | ✅ Done |
| Incremental Load Logic   | 🔄 Optional |
| Trigger for Automation   | 🔄 Optional |

This was a great exercise in cloud-based data movement using **Azure Data Factory**! 💙

