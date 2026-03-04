from pyspark.sql import SparkSession
import sys

def test_spark():
    spark = SparkSession.builder \
        .appName("SystemHealthCheck") \
        .getOrCreate()

    print("Checking Spark Connectivity...")
    data = [("Kafka", 1), ("Spark", 2), ("Airflow", 3), ("Cassandra", 4)]
    df = spark.createDataFrame(data, ["Tool", "Status"])
    
    print("DataFrame Created Successfully:")
    df.show()

    print("Spark Health Check: SUCCESS")
    spark.stop()

if __name__ == "__main__":
    test_spark()
