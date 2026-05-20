from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['tienda_instrumentos']
productos_collection = db['productos']

@app.route('/')
def index():
    return redirect(url_for('listar_productos'))

@app.route('/products')
def listar_productos():
    productos = list(productos_collection.find())
    return render_template('listar.html', productos=productos)

@app.route('/products/new', methods=['GET', 'POST'])
def crear_producto():
    if request.method == 'POST':
        nuevo_producto = {
            'nombre': request.form['nombre'],
            'descripcion': request.form['descripcion'],
            'precio': float(request.form['precio']),
            'stock': int(request.form['stock']),
            'categoria': request.form['categoria'],
            'imagen': request.form['imagen']
        }
        productos_collection.insert_one(nuevo_producto)
        return redirect(url_for('listar_productos'))
    
    return render_template('crear.html')

@app.route('/products/<id>')
def ver_producto(id):
    producto = productos_collection.find_one({'_id': ObjectId(id)})
    return render_template('detalle.html', producto=producto)

if __name__ == '__main__':
    app.run(debug=True)