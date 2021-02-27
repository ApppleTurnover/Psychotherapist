from flask import Flask, jsonify

import os

from airtable import Airtable

table = Airtable('app1dlRnFMmkTqj78', 'Psychotherapists', api_key=os.environ['api_key'])

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():
    return jsonify(table.get_all())


if __name__ == '__main__':
    app.run()
