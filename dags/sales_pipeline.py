"""
Collaborative Sales Pipeline - Initial Version
This DAG will be modified during the webinar to demonstrate Git collaboration
"""


from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract_sales_data():
    """Extract sales data from POS system"""
    return {"records": 1000, "source": "POS_API"}

def transform_sales_data(**context):
    """Basic sales data transformations"""
    return {"records_processed": 1000, "quality_checks": "passed"}

def load_to_warehouse(**context):
    """Load processed data to warehouse"""
    return {"rows_inserted": 1000, "table": "sales_facts"}


def calculate_discounts():
    """Calculate discount percentages - TO BE ADDED"""
    return {"rows_inserted": 1000, "quality_checks": "passed"}

with DAG(
    'sales_pipeline',
    start_date=datetime(2025, 1, 1),
    schedule='@daily',
    catchup=False
) as dag:

    extract_sales = PythonOperator(
        task_id='extract_sales',
        python_callable=extract_sales_data
    )

    transform_sales = PythonOperator(
        task_id='transform_sales',
        python_callable=transform_sales_data
    )

    load_sales = PythonOperator(
        task_id='load_sales',
        python_callable=load_to_warehouse
    )
    extract_sales >> transform_sales >> load_sales


