from google.cloud import bigquery

# Import custom packages
from src.config import *

# Initialize the BQ client
bq_client = bigquery.Client(project=BQ_PROJECT_ID)

def delete_bq_table(
	dataset_id: str,
	table_id: str,
) -> None:
	"""
	Deletes the provided BigQuery table from the provided dataset.

	Args:
		dataset_id: The dataset to delete the table from
		table_id: The table to delete
	"""
	
	bq_client.delete_table(
		f"{BQ_PROJECT_ID}.{dataset_id}.{table_id}",
		not_found_ok=True,
	)

	return

def delete_bq_dataset(
	dataset_id: str,
) -> None:
	"""
	Deletes the provided BQ dataset and all the tables within it.	

	Args:
		dataset_id: The dataset to delete
	"""

	bq_client.delete_dataset(
		dataset_id=f"{BQ_PROJECT_ID}.{dataset_id}",
		delete_contents=True,
		not_found_ok=True,
	)
	
	return

