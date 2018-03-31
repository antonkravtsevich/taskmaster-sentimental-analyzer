from flask import Flask, jsonify, request
import sentiment_processing as sp

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    json = request.get_json(silent=True)
    polarity = sp.get_polarity(json['raw_text'])
    return(jsonify({'status':'ok', 'polarity':polarity}), 200)


def main():
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    main()