from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys, os
sys.path.insert(0, os.path.abspath("/mnt/data/Week-05/azure_airflow_project"))

from export_formats import export_all_formats
from upload_to_blob import upload_files

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

dag = DAG(
    'db_to_azure_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
)

TABLE_NAME = "products"

export_task = PythonOperator(
    task_id='export_to_formats',
    python_callable=export_all_formats,
    op_args=[TABLE_NAME],
    dag=dag
)

upload_task = PythonOperator(
    task_id='upload_to_blob',
    python_callable=upload_files,
    op_args=[TABLE_NAME],
    dag=dag
)

export_task >> upload_task
