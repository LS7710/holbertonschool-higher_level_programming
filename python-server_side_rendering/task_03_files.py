from flask import Flask, render_template, request, json
import csv

app = Flask(__name__)

def read_json_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def read_csv_file(filename):
    products = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    if source == 'json':
        products = read_json_file('products.json')
    elif source == 'csv':
        products = read_csv_file('products.csv')
    else:
        return render_template('product_display.html', error='Wrong source')

    if product_id:
        try:
            product_id = int(product_id)
            products = [product for product in products if product['id'] == product_id]
            if not products:
                return render_template('product_display.html', error='Product not found')
        except ValueError:
            return render_template('product_display.html', error='Invalid id')

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
