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
    query = {}

    nombre = request.args.get('nombre')
    if nombre:
        query['nombre'] = {'$regex': nombre, '$options': 'i'}

    categoria = request.args.get('categoria')
    if categoria:
        query['categoria'] = {'$regex': categoria, '$options': 'i'}

    precio_min = request.args.get('precio_min')
    precio_max = request.args.get('precio_max')

    if precio_min or precio_max:
        query['precio'] = {}
        if precio_min:
            query['precio']['$gte'] = float(precio_min)
        if precio_max:
            query['precio']['$lte'] = float(precio_max)

    productos = list(productos_collection.find(query))
    return render_template('listar.html', productos=productos)

@app.route('/products/new', methods=['GET', 'POST'])
def crear_producto():
    if request.method == 'POST':
        imagen_url = request.form['imagen'].strip()
        if not imagen_url:
            imagen_url = '/static/default.png'

        nuevo_producto = {
            'nombre': request.form['nombre'],
            'descripcion': request.form['descripcion'],
            'precio': float(request.form['precio']),
            'stock': int(request.form['stock']),
            'categoria': request.form['categoria'],
            'imagen': imagen_url
        }
        productos_collection.insert_one(nuevo_producto)
        return redirect(url_for('listar_productos'))
    
    return render_template('crear.html')

@app.route('/products/<id>')
def ver_producto(id):
    producto = productos_collection.find_one({'_id': ObjectId(id)})
    return render_template('detalle.html', producto=producto)

@app.route('/products/<id>/edit', methods=['GET', 'POST'])
def editar_producto(id):
    if request.method == 'POST':
        imagen_url = request.form['imagen'].strip()
        if not imagen_url:
            imagen_url = '/static/default.png'

        productos_collection.update_one(
            {'_id': ObjectId(id)},
            {'$set': {
                'nombre': request.form['nombre'],
                'descripcion': request.form['descripcion'],
                'precio': float(request.form['precio']),
                'stock': int(request.form['stock']),
                'categoria': request.form['categoria'],
                'imagen': imagen_url
            }}
        )
        return redirect(url_for('listar_productos'))
    
    producto = productos_collection.find_one({'_id': ObjectId(id)})
    return render_template('editar.html', producto=producto)

@app.route('/products/<id>/delete', methods=['GET', 'POST'])
def eliminar_producto(id):
    if request.method == 'POST':
        productos_collection.delete_one({'_id': ObjectId(id)})
        return redirect(url_for('listar_productos'))
    
    producto = productos_collection.find_one({'_id': ObjectId(id)})
    return render_template('eliminar.html', producto=producto)

if __name__ == '__main__':
    app.run(debug=True)