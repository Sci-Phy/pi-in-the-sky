from flask import Flask, jsonify, request, render_template
import simplejson as json
app = Flask(__name__)

@app.route('/data', methods=['GET', 'POST'])
def data():
    with open('data.json') as json_file:
        data = json.load(json_file)
    return jsonify(data)
