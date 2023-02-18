from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'verify_cluster_kubernetes',
    default_args=default_args,
    start_date=datetime(2020, 1, 1),
    schedule_interval=timedelta(days=1)
)

t1 = BashOperator(
    task_id='run_this_first',
    bash_command='echo 1',
    queue='kubernetes',
    dag=dag)

t2 = BashOperator(
    task_id='run_this_last',
    bash_command='echo 2',
    queue='kubernetes',
    dag=dag)

t2.set_upstream(t1)
