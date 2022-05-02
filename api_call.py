from main import api_calls
from flask import Flask
import main
import json
from index_comparison import indexComparison

app = Flask(__name__)


@app.route('/currency')
def currency():
    return "Hello World"


@app.route('/')
def hello():
    thisdict = {"ticker": "msft", "index Comparison": indexComparison('msft')}

    return json.dumps(thisdict)


app.run()
