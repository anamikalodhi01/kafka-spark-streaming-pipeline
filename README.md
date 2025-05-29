# Kafka-Spark-Streaming-Pipeline

A real-time data streaming pipeline that ingests and processes Wikipedia Clickstream data using **Apache Kafka** and **Apache Spark Structured Streaming**.



##  About the Dataset

This project uses the [Wikipedia Clickstream Dataset (January 2017)](https://dumps.wikimedia.org/other/clickstream/2017/2017-01/). It contains aggregated counts of how often a user navigated from one Wikipedia article to another.

**Columns:**
- `prev`: The previous article
- `curr`: The current article
- `type`: Type of referrer (e.g. "link", "external", "other")
- `n`: Number of occurrences


## Tech Stack

- **Apache Kafka** – Event streaming platform
- **Apache Spark Structured Streaming** – Stream processing engine
- **Python** – For Kafka producer and Spark consumer scripts


## Project Structure

kafka-spark-streaming-pipeline/
# ├── kafka_producer.py # Kafka producer sending clickstream data
# ├── spark_consumer.py # Spark consumer processing Kafka stream
# ├── sample_clickstream.tsv # Sample subset of the Clickstream dataset
# ├── README.md # Documentation





##  Setup Instructions

###  Prerequisites

- Python 3.x
- Apache Kafka & Zookeeper
- Apache Spark
- Python packages:
  ```bash
  pip install kafka-python pyspark

## Running the Pipeline
### 1. Start Kafka and Zookeeper

# Start Zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties

# Start Kafka broker
bin/kafka-server-start.sh config/server.properties

# Create Kafka topic
bin/kafka-topics.sh --create --topic clickstream-data --bootstrap-server localhost:9092


### 2. Start the Kafka Producer
python kafka_producer.py
- Streams data from sample_clickstream.tsv into the Kafka topic clickstream-data.

### 3. Start the Spark Consumer
spark-submit spark_consumer.py
- Connects to the Kafka topic and processes real-time clickstream events.

