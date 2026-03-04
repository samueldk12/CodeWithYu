# Data Engineering Pipeline with Apache Iceberg

This project implements a complete, containerized Data Engineering pipeline stack.

## Technology Stack
- **Apache Airflow**: Orchestration and scheduling (CeleryExecutor).
- **Apache Spark**: Distributed data processing.
- **Apache Kafka**: Real-time event streaming.
- **Apache Iceberg**: Data lakehouse table format.
- **Trino**: Distributed SQL query engine.
- **Cassandra**: NoSQL storage.
- **Elasticsearch**: Search and analytics.
- **RabbitMQ**: Message broker.
- **Redis**: Cache and Celery broker.
- **Prometheus**: Monitoring.
- **PostgreSQL**: Metadata storage.

## Getting Started

### Prerequisites
- Docker & Docker Compose
- Windows (via start.bat) or Linux/WSL (via start.sh)

### Running the System
To start the entire infrastructure:
```bash
./start.bat
```

### Access Ports
- **Airflow**: http://localhost:8082 (Log: airflow / airflow)
- **Celery Flower**: http://localhost:5555
- **Spark Master UI**: http://localhost:8080
- **Kafka Control Center**: http://localhost:9021
- **Trino UI**: http://localhost:8083
- **Elasticsearch**: http://localhost:9200
- **RabbitMQ Management**: http://localhost:15672 (guest/guest)
- **Prometheus**: http://localhost:9090
- **Cassandra**: localhost:9042

## Testing Integration
A health check DAG is included (01_pipeline_health_check).

To test Apache Iceberg integration manually:
```bash
docker exec spark-master spark-submit --master spark://spark-master:7077 /opt/bitnami/spark/apps/test_iceberg.py
```

## Project Structure
- airflow/: DAGs, logs, and plugins.
- spark/: Spark apps and configuration.
- trino/: Catalog configurations.
- prometheus/: Monitoring configuration.
- docker-compose.yml: Infrastructure definition.
- start.bat: Bootstrap script for Windows.
