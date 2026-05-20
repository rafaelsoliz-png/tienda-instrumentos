from flask import Flask, render_template, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['tienda_instrumentos']
productos_collection = db['productos']

@app.route('/')
def index():
    return redirect(url_for('listar_productos'))

@app.route('/products')
def listar_productos():
    return render_template('listar.html')

if __name__ == '__main__':
    app.run(debug=True) 