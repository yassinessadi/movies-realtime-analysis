from flask import Flask
import json
import pandas as pd


app = Flask(__name__)


@app.route('/get_movies/<int:count>', methods=['GET'])

def index(count):
    df = pd.read_json(path_or_buf='../data/output.json',orient='records')

    res = df.sample(n=count).to_json(orient='records')

    return json.loads(res)

if __name__ == '__main__':
    app.run(debug=True)