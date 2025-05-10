
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_extract
from pyspark.sql.types import StringType

# Initialize Spark session
spark = SparkSession.builder \
    .appName("NginxLogsKafkaStreaming") \
    .config("spark.sql.shuffle.partitions", "2") \
    .getOrCreate()

# Read from Kafka
kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "flume-logs") \
    .option("startingOffsets", "earliest") \
    .load()

# Convert Kafka value (binary) to string
logs_df = kafka_df.selectExpr("CAST(value AS STRING)")

# Debug: Print raw logs to verify format
raw_query = logs_df.writeStream \
    .format("console") \
    .outputMode("append") \
    .trigger(processingTime="10 seconds") \
    .start()

# Parse the Nginx log line using regex
parsed_df = logs_df.select(
    regexp_extract(col("value"), r'^(\S+)', 1).alias("ip"),
    regexp_extract(col("value"), r'"([^"]+)"', 1).alias("request"),
    regexp_extract(col("value"), r'" (\d+) ', 1).alias("status_code")
)

# Aggregate: Count requests by status code
status_counts = parsed_df.groupBy("status_code").count()

# Output to console every 10 seconds
query = status_counts.writeStream \
    .outputMode("complete") \
    .format("console") \
    .trigger(processingTime="10 seconds") \
    .start()

# Wait for the stream to terminate
query.awaitTermination()
