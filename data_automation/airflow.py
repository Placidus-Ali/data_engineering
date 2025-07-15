# Sample data automation with airflow 

# Using Dag

dag = DAG("my_dag" start_date =datetime(2020, 12, 1))

# Define task for the Dag
start_cluster = StartClusterOperator(start_id = 'start_cluster', dag=dag)
input_athlete_data = SparkJobOperator(start_id = 'input_athlete_data', dag=dag)
input_venue_data = SparkJobOperator(start_id = 'input_venue_data', dag=dag)

# Setup Dependency Flow
start_cluster.set_downstream(input_athlete_data)
input_athlete_data = set_downstream(enrich_athlete_data)
input_venue_data = set_downstream(enrich_athlete_data)

