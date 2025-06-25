from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

dag = DAG(
    'Data_souls',
    start_date=datetime(2025, 1, 8),
    schedule_interval='*/5 * * * *',
    catchup=False,
)

t1 = BashOperator(
        task_id='print_date',
        bash_command='pwd',
        dag=dag,
    )

t2 = BashOperator(
        task_id='sleep',
        bash_command='sleep 5',
        dag=dag,
    )

run = BashOperator(
        task_id = 'run',
        bash_command='python /mnt/c/Users/Hari/airflow-docker/pyfile/hello.py',
        dag=dag,
    )

t1 >> t2 >> run 
