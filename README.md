# Data Engineering Pipeline with Apache Iceberg

This project implements a complete, containerized Data Engineering pipeline stack.

## 🛠️ Technology Stack
- **Apache Airflow**: Orchestration and scheduling.
- **Apache Spark**: Distributed data processing.
- **Apache Kafka**: Real-time event streaming.
- **Apache Iceberg**: Data lakehouse table format (Hadoop Catalog).
- **Cassandra**: NoSQL storage for processed data.
- **PostgreSQL**: Metadata storage for Airflow.
- **Confluent Control Center**: Kafka monitoring and management.

## 🚀 Getting Started

### Prerequisites
- Docker & Docker Compose
- Windows (via `start.bat`) or Linux/WSL (via `start.sh`)

### Running the System
To start the entire infrastructure:
```bash
./start.bat
```

### Access Ports
- **Airflow**: [http://localhost:8082](http://localhost:8082) (Log: `airflow` / `airflow`)
- **Spark Master UI**: [http://localhost:8080](http://localhost:8080)
- **Kafka Control Center**: [http://localhost:9021](http://localhost:9021)
- **Schema Registry**: [http://localhost:8081](http://localhost:8081)
- **Cassandra**: `localhost:9042`

## 🧪 Testing Integration
A health check DAG is included (`01_pipeline_health_check`) to verify connectivity between all services.

To test **Apache Iceberg** integration manually:
```bash
docker exec spark-master spark-submit --master spark://spark-master:7077 /opt/bitnami/spark/apps/test_iceberg.py
```

## 📂 Project Structure
- `airflow/`: DAGs, logs, and plugins.
- `spark/`: Spark apps and configuration.
- `docker-compose.yml`: Infrastructure definition.
- `start.bat`: Bootstrap script for Windows.
