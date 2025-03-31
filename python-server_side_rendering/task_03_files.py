#!/usr/bin/python3
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)
    
def read_csv():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
            return products
        
@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    else:
        return render_template('product_display.html', error="Wrong source")
    
    if product_id:
        product = next((p for p in products if p['id'] == product_id), None)
        if product:
            return render_template('product_display.html', "Product=product")
        else:
            return render_template('product_display.html', error="Product not found")
        
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
