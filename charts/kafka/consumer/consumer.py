# kafka/consumer/consumer.py
from kafka import KafkaConsumer
import json
import requests
import logging
import socket
from datetime import datetime

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize Kafka consumer
consumer = KafkaConsumer(
    'logs',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='log-consumer-group'
)

# Define Elasticsearch endpoint
es_url = "http://elasticsearch:9200/logs/_doc"

hostname = socket.gethostname()

for msg in consumer:
    try:
        # Enrich log
        enriched_log = msg.value
        enriched_log["@timestamp"] = datetime.utcnow().isoformat()
        enriched_log["source_host"] = hostname

        # Send to Elasticsearch
        response = requests.post(es_url, json=enriched_log)
        response.raise_for_status()
        logging.info(f"Log sent to Elasticsearch: {enriched_log}")
    except Exception as e:
        logging.error(f"Failed to send log: {e}")