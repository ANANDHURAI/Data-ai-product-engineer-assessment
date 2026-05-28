from google.cloud import bigquery
import logging
import os

logging.basicConfig(level=logging.INFO)

# Set credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service_account.json"

PROJECT_ID = "sound-country-464003-n4"
DATASET_ID = "weather_pipeline"
TABLE_ID = "weather_data"


def load_to_bigquery(df):

    try:
        client = bigquery.Client(project=PROJECT_ID)

        table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"
        job_config = bigquery.LoadJobConfig(
            write_disposition="WRITE_TRUNCATE"
        )

        job = client.load_table_from_dataframe(
            df,
            table_ref,
            job_config=job_config
        )

        job.result()

        logging.info("Data loaded successfully into BigQuery")

    except Exception as e:
        logging.error(f"BigQuery upload failed: {e}")