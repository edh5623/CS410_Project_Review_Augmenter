"""
Flask server to run Python code from JavaScript
"""

from flask import Flask, request
from redcircle import *

app = Flask(__name__)


@app.route('/tra/query')
def query():
    item_url = request.args.get("item_url")
    query = request.args.get("query_text")
    print("Item URL: " + item_url)
    print("Query: " + query)
    results_dict = get_top_reviews_and_ratings(query, item_url)

    return json.dumps(results_dict)


if __name__ == '__main__':
    app.run(threaded=False)
