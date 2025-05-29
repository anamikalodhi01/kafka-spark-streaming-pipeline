from kafka import KafkaProducer
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: v.encode('utf-8')
)

with open('/mnt/c/kafka_2.12-3.9.1/2017_01_en_clickstream.tsv', 'r', encoding='utf-8') as file:
    for line in file:
        producer.send('clickstream', value=line.strip())  # topic name matches Spark consumer
        print("Sent:", line.strip())
        time.sleep(0.5)

producer.flush()
producer.close()
