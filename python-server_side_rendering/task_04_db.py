#!/usrbin/python3
import csv
from flask import Flask, render_template, request
import json
import sqlite3

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
    elif source == "sql":
        try:
            products = parse_sql_data("products.db", id)
        except Exception as err:
            error = err
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

def parse_sql_data(db, id=None):
    """Parses SQL data"""
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    query = "SELECT * FROM Products"
    if id:
        query += f" WHERE id = {id}"

    cursor.execute(query)

    products = []
    for row in cursor.fetchall():
        products.append({"id": row[0], "name": row[1], "category": row[2], "price": row[3]})

    return products

if __name__ == '__main__':
    app.run(debug=True, port=5000)
