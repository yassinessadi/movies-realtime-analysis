from confluent_kafka import Producer
import requests
import json
import time

topic = "yassinecounter"
kafka_config = {
    "bootstrap.servers": "localhost:9092", 
}

producer = Producer(kafka_config)

while True:
    response = requests.get("http://127.0.0.1:5000/get_movies/1")
    time.sleep(2)
    if response.status_code == 200:
        data = json.dumps(response.json())
        producer.produce(topic, key="randomovie", value=data)
        producer.flush()
        print(response.json())
    else:
        print(response.status_code)