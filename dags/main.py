from airflow import DAG
import pendulum
from datetime import datetime, timedelta

from api.video_stats import (
    get_playlist_id,
    get_video_ids,
    extract_video_data,
    save_to_json,
)

# Define the local timezone
local_tz = pendulum.timezone("America/Bogota")

# Default Args
default_args = {
    "owner": "jhongarcia",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "max_active_runs": 1,
    "dagrun_timeout": timedelta(hours=1),
    "start_date": datetime(2025, 1, 1, tzinfo=local_tz),
}

with DAG(
    dag_id="produce_json",
    default_args=default_args,
    description="A DAG to produce JSON file with raw data",
    schedule="0 14 * * *",  # Everyday at 2 PM Bogotá time
    catchup=False,
) as dag:

    # Define tasks
    playlist_id = get_playlist_id()
    video_ids = get_video_ids(playlist_id)
    extract_data = extract_video_data(video_ids)
    save_to_json_task = save_to_json(extract_data)

    # Dependencies
    playlist_id >> video_ids >> extract_data >> save_to_json_task
