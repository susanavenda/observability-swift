

from kafka import KafkaProducer
import json
import time
import random
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Sample log levels
log_levels = ['INFO', 'WARNING', 'ERROR', 'DEBUG']

# Produce logs every second
try:
    while True:
        log_message = {
            "level": random.choice(log_levels),
            "message": "Simulated application log entry",
            "timestamp": time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
        }

        # Send log to Kafka topic 'logs'
        producer.send('logs', log_message)
        logging.info(f"Sent log: {log_message}")
        time.sleep(1)

except KeyboardInterrupt:
    logging.info("Stopping log producer...")
    producer.close()