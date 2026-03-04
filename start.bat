@echo off
echo [INFO] Inicializando o Sistema de Pipeline de Dados...

if not exist "airflow\dags" mkdir "airflow\dags"
if not exist "airflow\logs" mkdir "airflow\logs"
if not exist "airflow\plugins" mkdir "airflow\plugins"
if not exist "spark\apps" mkdir "spark\apps"
if not exist "spark\data" mkdir "spark\data"

echo [INFO] Subindo os containers do Docker...
docker-compose up -d

echo.
echo ========================================================
echo [SUCESSO] O sistema esta sendo iniciado em segundo plano!
echo ========================================================
echo Portas principais:
echo - Airflow: http://localhost:8082 (User/Pass: airflow/airflow)
echo - Spark Master UI: http://localhost:8080
echo - Kafka Control Center: http://localhost:9021
echo - Schema Registry: http://localhost:8081
echo - Cassandra: localhost:9042
echo ========================================================
echo.
pause
