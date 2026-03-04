from pyspark.sql import SparkSession

def test_iceberg():
    spark = SparkSession.builder \
        .appName("IcebergTest") \
        .getOrCreate()

    print("--- Testando Apache Iceberg ---")
    
    spark.sql("CREATE TABLE IF NOT EXISTS local.db.test_table (id bigint, data string) USING iceberg")
    
    spark.sql("INSERT INTO local.db.test_table VALUES (1, 'Iceberg está funcionando!')")
    
    print("Dados na tabela Iceberg:")
    spark.sql("SELECT * FROM local.db.test_table").show()
    
    print("--- Sucesso: Iceberg integrado com Spark! ---")
    spark.stop()

if __name__ == "__main__":
    test_iceberg()
