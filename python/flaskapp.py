from flask import Flask, jsonify, request
from redcircle import *

app = Flask(__name__)


@app.route('/tra/reviews')
def reviews():
    return parse_reviews()

@app.route('/tra/query')
def query():
    item_url = request.args.get("item_url")
    query = request.args.get("query_text")
    print("Item URL: " + item_url)
    print("Query: " + query)
    return parse_reviews()


if __name__ == '__main__':
    app.run()
