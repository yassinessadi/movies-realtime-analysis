from flask import Flask, jsonify
from neo4j import GraphDatabase
import json
import pandas as pd


app = Flask(__name__)


@app.route('/get_movies/<int:count>', methods=['GET'])

def index(count):
    df = pd.read_json(path_or_buf='../data/output.json',orient='records')

    res = df.sample(n=count).to_json(orient='records')

    return json.loads(res)

# Route for movie recommendations
@app.route('/recommendations/<int:userId>', methods=['GET'])
def get_movie_recommendations(userId):

    # Your Neo4j connection details
    URI = "bolt://localhost:7687"
    AUTH = ("", "")

    # Connect to Neo4j
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        with driver.session() as session:
            # Run the Cypher query to get movie recommendations
            result = session.run(
                '''
                    MATCH (u:User {userId: $userId})-[r1:RATED]->(m:Movie)<-[r2:RATED]-(other:User)-[r3:RATED]->(rec:Movie)
                    WHERE NOT EXISTS((u)-[:RATED]->(rec))
                    RETURN rec.title, AVG(r3.rating) AS avg_rating
                    ORDER BY avg_rating DESC
                    LIMIT 10
                ''',
                userId=userId
            )

            # Process the query results
            recommendations = []
            for record in result:
                movie_title = record['rec.title']
                avg_rating = record['avg_rating']
                recommendations.append({'title': movie_title, 'avg_rating': avg_rating})

    # Return the movie recommendations as JSON response
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)