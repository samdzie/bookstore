import requests
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world!'


@app.route('/customer/<customer_id>')
def get_sales_from_customer(customer_id):
    customer = requests.get(
        'http://customer-service:5000/customer/' + customer_id).json()
    return jsonify({
        'customer' : customer
    })
