from flask import Flask,jsonify
import json
import pandas as pd

df = pd.read_json(orient='records',path_or_buf='../data/output.json')


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    res = df.head(10).to_json(orient='records')
    result = json.loads(res)
    return jsonify(result)
