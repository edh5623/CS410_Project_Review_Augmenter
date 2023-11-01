from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/tra/reviews')
def reviews():
    return jsonify('Hello World!')


if __name__ == '__main__':
    app.run()
