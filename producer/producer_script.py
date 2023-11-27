from confluent_kafka import Producer
import requests
import json
import logging

topic = "ratingmoviesapplication"
kafka_config = {
    "bootstrap.servers": "localhost:9092", 
}

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

producer = Producer(kafka_config)

while True:
    response = requests.get("http://127.0.0.1:5000/get_movies/1")
    if response.status_code == 200:
        data = json.dumps(response.json()[0])
        producer.produce(topic, key="key", value=data)
        producer.flush()
        #print(data)
        logger.info("Produced message: %s", data)
    else:
        print(response.status_code)
        logger.error("Failed to fetch movie data. HTTP status code: %d", response.status_code)
