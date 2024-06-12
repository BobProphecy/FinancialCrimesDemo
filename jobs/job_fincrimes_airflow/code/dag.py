import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
from airflow.decorators import task
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from k9tiu19yupnzbl8avioajw_.tasks import pipe_financial_crimes
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "K9tIu19yuPnzbL8aVIOAJw_", 
    schedule_interval = None, 
    default_args = {"owner" : "Prophecy", "ignore_first_depends_on_past" : True, "do_xcom_push" : True, "pool" : "2AGL95yk"}, 
    start_date = pendulum.today('UTC'), 
    end_date = pendulum.datetime(2024, 7, 1, tz = "UTC"), 
    catchup = True, 
    tags = []
) as dag:
    pipe_financial_crimes_op = pipe_financial_crimes()
