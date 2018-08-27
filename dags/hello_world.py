from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators import HelloWorldOperator

default_args = {
    'owner': 'silverlight',
    'depends_on_past': False,
    'start_date': datetime(2015, 6, 1),
}

dag = DAG('hello_world', default_args=default_args, schedule_interval=timedelta(seconds=1))


dummy_task = DummyOperator(task_id='dummy_task', dag=dag)

helloword_task = HelloWorldOperator(my_params='This is a test.',
                                task_id='helloworld_task', dag=dag)

helloword_task.set_upstream(dummy_task)
