from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world!'


@app.route('/customer/<customer_id>')
def get_customer(customer_id):
    return jsonify({
        'name' : 'jane doe',
    })
