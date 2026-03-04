from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import socket

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

def check_socket(host, port):
    try:
        with socket.create_connection((host, port), timeout=5):
            print(f"Connection to {host}:{port} successful!")
            return True
    except Exception as e:
        print(f"Connection to {host}:{port} failed: {e}")
        raise e

with DAG(
    '01_pipeline_health_check',
    default_args=default_args,
    description='DAG para verificar a integração entre Airflow, Kafka, Spark e Cassandra',
    schedule_interval=None,
    catchup=False,
    tags=['test', 'infrastructure'],
) as dag:

    check_kafka = PythonOperator(
        task_id='verify_kafka',
        python_callable=check_socket,
        op_kwargs={'host': 'broker', 'port': 29092},
    )

    check_cassandra = PythonOperator(
        task_id='verify_cassandra',
        python_callable=check_socket,
        op_kwargs={'host': 'cassandra', 'port': 9042},
    )

    check_spark = PythonOperator(
        task_id='verify_spark_master',
        python_callable=check_socket,
        op_kwargs={'host': 'spark-master', 'port': 7077},
    )

    check_iceberg = BashOperator(
        task_id='verify_iceberg',
        bash_command='docker exec spark-master spark-submit --master spark://spark-master:7077 /opt/bitnami/spark/apps/test_iceberg.py',
    )

    log_success = BashOperator(
        task_id='log_system_health',
        bash_command='echo ">>> TODAS AS FERRAMENTAS ESTÃO ONLINE E ACESSÍVEIS! <<<"',
    )

    [check_kafka, check_cassandra, check_spark] >> check_iceberg >> log_success
