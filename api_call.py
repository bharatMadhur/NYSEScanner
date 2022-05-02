from main import api_calls
from flask import Flask

app = Flask(__name__)

@app.route('/currency')
def currency():
    return "Hello World"
@app.route('/')
def hello():
    send_data = api_calls()
    return send_data




app.run()
