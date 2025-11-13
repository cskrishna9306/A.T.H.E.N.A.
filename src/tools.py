
# Import custom packages
from src.config import (
	bq_client,
	BQ_PROJECT_ID,
	BQ_REGION,
)

def get_top_k_bq_users(
	k: int,
):
	"""
	Gets the top k users w/ the most query usage from the BigQuery project.

	Args:
		k: The number of users to get
	"""

	query = f"""
	SELECT
		user_email,
		SUM(total_bytes_processed) / 1024 / 1024 / 1024 AS total_gb_processed,
		AVG(total_bytes_processed) / 1024 / 1024 / 1024 AS avg_gb_processed,
		(SUM(total_bytes_processed) / 1024 / 1024 / 1024) * 0.0048 AS total_cost
	FROM {BQ_REGION}.INFORMATION_SCHEMA.JOBS
	WHERE job_type = "QUERY"
	GROUP BY 1
	ORDER BY 2 DESC
	LIMIT {k}
	"""

	# Start the query job
	query_job = bq_client.query(query).result()
	
	# print(query_job.to_dataframe())
	
	return query_job.to_dataframe()

def get_top_k_bq_tables(
	k: int,
):
	"""
	Gets the top k tables from the BigQuery project.

	Args:
		k: The number of tables to get
	"""

	query = f"""
	SELECT
		project_id,
		table_name,
		creation_time,
		total_rows,
		total_physical_bytes / 1024 / 1024 / 1024 AS size_gb,
	FROM {BQ_REGION}.INFORMATION_SCHEMA.TABLE_STORAGE
	WHERE deleted=FALSE
 	ORDER BY size_gb DESC
	LIMIT {k}
	"""

	# Start the query job
	query_job = bq_client.query(query).result()
	
	print(query_job.to_dataframe())
	
	return query_job.to_dataframe()


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

