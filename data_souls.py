from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

dag = DAG(
    'Data_souls',
    start_date=datetime(2025, 1, 8),
    schedule_interval='*/5 * * * *',
    catchup=False,
)

t_show_time = BashOperator(
    task_id='show_time',
    bash_command='date', 
)

run = BashOperator(
        task_id = 'run',
        bash_command='cd /mnt/c/airflow/scripts && python main.py',
        dag=dag,
)

t_show_time >> run
  
