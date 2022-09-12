from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2020, 1, 1),
}

dag = DAG(
    'verify_cluster_kubernetes',
    default_args=default_args,
    schedule_interval=timedelta(days=1))

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
