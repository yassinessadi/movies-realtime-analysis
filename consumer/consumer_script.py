from neo4j import GraphDatabase
from confluent_kafka import Consumer,  KafkaError
import json

URI = "bolt://localhost:7687"

AUTH = ("", "")

topic = "ratingmoviesapplication"

kafka_group_id = 'group-id'

kafka_config = {
    'group.id': kafka_group_id,
    "bootstrap.servers": "localhost:9092", 
}

consumer = Consumer(kafka_config)
consumer.subscribe([topic])

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    # print(msg.value())

    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            print(f"Reached end of partition {msg.topic()} [{msg.partition()}]")
        else:
            print(f"Error: {msg.error()}")
    else:
        print(f"Received message: {msg.value()}")
        user = {}
        movie = {}
        genre = {}


        data = json.loads(msg.value())

        #creation of nodes
        user['userId'] = data['userId']
        user['rating'] = data['rating']
        user['timestamp'] = data['timestamp']

        movie['movieId'] = data['movie']['movieId']
        movie['title'] = data['movie']['title']
        movie['genres'] = data['movie']['genres']

        with GraphDatabase.driver(URI, auth=AUTH) as client:
    
            # Check the connection
            client.verify_connectivity()
            
            # Creation movie node
            records, summary, keys = client.execute_query(
                "MERGE (m:Movie {movieId: $movieId,title: $title}) RETURN m.movieId AS movieId;",
            movieId=movie['movieId'],
            title=movie['title'],
            database_="memgraph",
            )
            # Creation user node
            records, summary, keys = client.execute_query(
                "MERGE (u:User {userId: $userId}) ",
            userId=user['userId'],
            rating=user['rating'],
            timestamp=user['timestamp'],
            database_="memgraph",
            )
            # Creation of genre node
            for genre in movie['genres']:
                records, summary, keys = client.execute_query(
                    "MERGE (g:Genre {genre: $genre}) ",
                    genre=genre,
                    database_="memgraph"
                )
            records, summary, keys = client.execute_query(
                """
                MATCH (u:User {userId: $userId}), (m:Movie {movieId: $movieId})
                MERGE (u)-[r:RATED {rating: ToFloat($rating), timestamp: $timestamp}]->(m)
                WITH m
                UNWIND $genres AS genre
                MERGE (m)-[r:OF_GENRE {name: genre}]->(g:Genre {genre: genre})
                """,
                userId=user['userId'],
                rating=user['rating'],
                movieId=movie['movieId'],
                genres= movie["genres"],
                timestamp=user['timestamp'],
                database_="memgraph"
            )
            for record in records:
                print(record["movieId"])
            #creation relationship



# with GraphDatabase.driver(URI, auth=AUTH) as client:
    
#     # Check the connection
#     client.verify_connectivity()

#     records, summary, keys = client.execute_query(
#         "MERGE (m:Movie {userId: $userId,movie:{ movieId: $movieId,title: $title,genres: $genres},rating: $rating, timestamp: $timestamp }) RETURN m.userId AS userId;",
#         userId=365,
#         movieId=7526,
#         title="Lord of the Rings: The Fellowship of the Ring, The (2001)",
#         genres=["Adventure", "Fantasy"],
#         rating=5,
#         timestamp=45554125,
#         database_="memgraph",
#     )

#     # Get the result
#     for record in records:
#         print(record["userId"])