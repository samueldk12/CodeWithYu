# Pipeline de Dados - CodeWithYu

Este projeto configura uma infraestrutura completa de pipeline de dados em tempo real conforme a arquitetura:
`API -> Airflow -> Kafka -> Spark -> Cassandra`

## Componentes Incluídos

- **Apache Airflow**: Orquestração de workflows.
- **Apache Kafka**: Streaming de dados (Mensageria).
- **Zookeeper**: Gerenciamento do cluster Kafka.
- **Schema Registry**: Gerenciamento de esquemas do Kafka.
- **Control Center**: Interface visual para o Kafka.
- **Apache Spark**: Processamento distribuído (1 Master + 2 Workers).
- **Cassandra**: Banco de dados NoSQL para destino final.
- **PostgreSQL**: Banco de dados para metadados do Airflow.

## Como Iniciar

### Windows
Basta clicar duas vezes no arquivo `start.bat`.

### Linux/macOS
Abra o terminal na pasta e execute:
```bash
chmod +x start.sh
./start.sh
```

## URLs de Acesso

| Serviço | URL | Credenciais |
| :--- | :--- | :--- |
| **Airflow** | [http://localhost:8082](http://localhost:8082) | `airflow` / `airflow` |
| **Spark Master** | [http://localhost:8080](http://localhost:8080) | - |
| **Kafka Control Center** | [http://localhost:9021](http://localhost:9021) | - |

## Estrutura de Pastas de Volume

- `airflow/dags`: Coloque seus scripts Python (DAGs) aqui.
- `spark/apps`: Coloque seus jobs do Spark (.py ou .jar) aqui.
- `spark/data`: Use para leitura/escrita de dados locais no Spark.
