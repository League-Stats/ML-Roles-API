import flask
import json
from flask import request, jsonify
import roleml

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Python API</h1><p>API home endpoint is functional.</p>"

@app.route('/api/roleml', methods=['POST'])
def roles():
    req_data = request.get_json()
    getMatch = req_data['match']
    getTimeline = req_data['timeline']
    match = json.loads(getMatch)
    timeline = json.loads(getTimeline)

    prediction = roleml.predict(match, timeline)
    return prediction

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)