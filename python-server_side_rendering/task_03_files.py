#!/usrbin/python3
import csv
from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json', 'r') as file:
        data = json.load(file)
        items = data.get("items")

    return render_template('items.html', items=items)

@app.route('/products')
def source():
    source = request.args.get("source")
    id = request.args.get("id")
    
    error = None
    products = []

    if source == "json":
        products = parse_json_data("products.json", id)
    elif source == "csv":
        products = parse_csv_data("products.csv", id)
    else:
        error = "Wrong source"

    if not error and id and len(products) == 0:
            error = "Product not found"

    return render_template('product_display.html', products=products, error_message=error)

def parse_json_data(filename, id=None):
    """Parses JSON data"""

    with open(filename, 'r') as file:
        data = json.load(file)

    products = []
    for row in data:
        if not id or int(id) == row["id"]:
            products.append(row)
    return products

def parse_csv_data(filename, id=None):
    """Parses CSV data"""

    with open(filename, 'r') as file:
        products = []
        rows = csv.reader(file)
        line_number = 0
        for row in rows:
            if line_number > 0 and (not id or (id == row[0])):
                products.append({"id": row[0], "name": row[1], "category": row[2], "price": row[3]})
            line_number += 1

    return products

if __name__ == '__main__':
    app.run(debug=True, port=5000)
