import logging
from airflow.operators.bash import BashOperator

logger = logging.getLogger(__name__)

SODA_PATH = "/opt/airflow/include/soda"
DATASOURCE = "pg_datasource"

def yt_elt_data_quality(schema):
    return BashOperator(
        task_id=f"soda_test_{schema}",
        bash_command=(
            f"soda scan "
            f"-d {DATASOURCE} "
            f"-c {SODA_PATH}/configuration.yml "
            f"-v SCHEMA={schema} "
            f"{SODA_PATH}/checks.yml"
        ),
    )