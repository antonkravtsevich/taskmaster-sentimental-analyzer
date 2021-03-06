from flask import Flask, jsonify, request
from flask_cors import CORS
from sentiment_processing import SentimentProcessor
from datetime import datetime

app = Flask(__name__)
CORS(app)
startTime = datetime.now()
sp = SentimentProcessor()


@app.route('/get_polarity', methods=['POST'])
def get_polarity():
    json = request.get_json(silent=True)
    polarity = sp.get_polarity(json['raw_text'])
    return(jsonify({'status': 'ok', 'polarity': polarity}), 200)


@app.route('/status', methods=['GET'])
def get_status():
    currTime = datetime.now()
    response = 'Uptime: {}'.format(currTime - startTime)
    return(response)


def main():
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    main()
