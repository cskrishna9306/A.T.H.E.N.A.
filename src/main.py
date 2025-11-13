from src.bigquery_agent import BigQueryAnalyst

if __name__ == "__main__":
    bigquery_agent = BigQueryAnalyst()
    response = bigquery_agent.run("Show me the top 5 largest tables by logical size in BigQuery.")
    print(response)

