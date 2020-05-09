from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import json
import time
import csv

import utils

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

dfs = utils.read_data()

@app.route('/data', methods = ['GET'])
@cross_origin()
def getAllData():
    return jsonify(dfs)

@app.route('/data/indicator', methods = ['POST'])
@cross_origin()
def getIndicatorData():
    ind = request.json['indicator']
    if ind not in dfs:
        return jsonify(error="Indicator not found")

    return jsonify(dfs[ind])

if __name__ == '__main__':
    app.run()