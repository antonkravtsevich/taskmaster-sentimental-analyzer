from flask import Flask, jsonify, request
import sentiment_processing as sp
from temp_storage import TempStorage
from datetime import datetime

app = Flask(__name__)
startTime = datetime.now()
tp = TempStorage()

@app.route('/', methods=['POST'])
def index():
    json = request.get_json(silent=True)
    polarity = sp.get_polarity(json['raw_text'])
    tp.add_new_record(text=json['raw_text'], polarity=polarity)
    return(jsonify({'status':'ok', 'polarity':polarity}), 200)


@app.route('/status', methods=['GET'])
def get_status():
    currTime = datetime.now()
    response = 'Uptime: {}<br><br>'.format(currTime - startTime)
    response += str(tp)
    return(response)


def main():
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    main()