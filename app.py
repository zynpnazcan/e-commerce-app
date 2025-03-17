from flask import Flask, render_template
app = Flask(name)
products = [{'id': 1, 'name': 'Telefon', 'price': 1000}, {'id': 2, 'name': 'Laptop', 'price':
5000}]
@app.route('/')
def home():
 return render_template('index.html', products=products)
if name == 'main':
 app.run(host='0.0.0.0', port=5000)