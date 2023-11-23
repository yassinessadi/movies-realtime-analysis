from neo4j import GraphDatabase
from pykafka import KafkaClient


URI = "bolt://localhost:7687"
AUTH = ("", "")



with GraphDatabase.driver(URI, auth=AUTH) as client:
    
    # Check the connection
    client.verify_connectivity()

    records, summary, keys = client.execute_query(
        "MERGE (m:Movie {userId: $userId,movie:{ movieId: $movieId,title: $title,genres: $genres},rating: $rating, timestamp: $timestamp }) RETURN m.userId AS userId;",
        userId=365,
        movieId=7526,
        title="Lord of the Rings: The Fellowship of the Ring, The (2001)",
        genres=["Adventure", "Fantasy"],
        rating=5,
        timestamp=45554125,
        database_="memgraph",
    )

    # Get the result
    for record in records:
        print(record["userId"])