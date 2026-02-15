# DE-ETL Project

# настроить зеркала в docker для скачивания!

# settings 
docker network connect bes-network postgres_source --alias postgres

# quick start
docker compose up -d minio
docker compose up -d postgres-source postgres-target
docker compose ps | grep postgres

docker compose up -d namenode
sleep 10
docker compose up -d datanode nodemanager resourcemanager historyserver

docker compose up -d hive-metastore hive-server

docker compose up -d spark-master spark-worker

docker compose up -d trino

docker compose up -d nessie

docker compose up -d kafka schema-registry conduktor-postgresql conduktor-console conduktor-monitoring

docker compose up -d nifi-zookeeper nifi

docker compose up -d jobmanager taskmanager

docker compose up -d airflow-db airflow
