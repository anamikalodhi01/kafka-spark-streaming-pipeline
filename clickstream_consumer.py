from pyspark.sql import SparkSession
from pyspark.sql.functions import expr

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Clickstream Analysis") \
      .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.13:4.0.0") \
    .getOrCreate()

spark.sparkContext.setLogLevel("INFO")

# Kafka parameters
kafka_bootstrap_servers = "localhost:9092"
topic = "clickstream"

# Read from Kafka
clickstream_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
    .option("subscribe", topic) \
    .load()

clickstream_df = clickstream_df.selectExpr("CAST(value AS STRING)") \
    .withColumn("split_data", expr("split(value, '\\t')")) \
    .selectExpr("split_data[0] as user", "split_data[1] as page")

# Write to console
query = clickstream_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .option("truncate", False) \
    .trigger(processingTime="5 seconds") \
    .start()

query.awaitTermination()










# from pyspark.sql import SparkSession

# def main():
#     spark = SparkSession.builder \
#         .appName("KafkaClickstreamToParquet") \
#         .getOrCreate()

#     kafka_df = spark.readStream.format("kafka") \
#         .option("kafka.bootstrap.servers", "localhost:9092") \
#         .option("subscribe", "clickstream") \
#         .load()

#     # Convert Kafka binary value to string
#     clickstream_df = kafka_df.selectExpr("CAST(value AS STRING) as message")

#     query = (
#         clickstream_df.writeStream
#         .format("parquet")  # or "json", "csv"
#         .option("path", "/tmp/clickstream_data")
#         .option("checkpointLocation", "/tmp/clickstream_checkpoint")
#         .trigger(processingTime="1 minute")  # batch interval
#         .start()
#     )

#     query.awaitTermination()

# if __name__ == "__main__":
#     main()
