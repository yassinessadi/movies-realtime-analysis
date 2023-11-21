from pykafka import KafkaClient


client = KafkaClient(hosts="localhost:9092")

print(client)
