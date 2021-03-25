from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from transformation.spark import run

dag = DAG(
    'elspot_etl', 
    description='ETL Pipeline for fetching elspot price data', 
    schedule_interval='0 12 * * *', 
    start_date=datetime(2017, 3, 20), 
    catchup=False
    )


hello_operator = PythonOperator()
