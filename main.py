# pip install Flask Flask-SQLAlchemy pyodbc 

from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import webbrowser

app = Flask(__name__)
CORS(app, resources={r"/pedidos/*": {"origins": "http://127.0.0.1:5001"}})

# Configura tu conexión según tu servidor SQL Server
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'mssql+pyodbc://sa:admin123@localhost/DB_PEDIDOS?driver=ODBC+Driver+17+for+SQL+Server'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de la tabla pedidos
class Pedido(db.Model):
    __tablename__ = 'pedidos'
    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    marca = db.Column(db.String(100), nullable=False)
    producto = db.Column(db.String(100), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Float, nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

# Obtener todos los pedidos o uno por ID
@app.route('/pedidos', methods=['GET'])
@app.route('/pedidos/<int:id>', methods=['GET'])
def get_pedidos(id=None):
    if id is None:
        pedidos = Pedido.query.all()
        return jsonify([{
            'id': p.id,
            'cliente': p.cliente,
            'categoria': p.categoria,
            'marca': p.marca,
            'producto': p.producto,
            'cantidad': p.cantidad,
            'precio': p.precio
        } for p in pedidos])
    else:
        pedido = Pedido.query.get(id)
        if pedido:
            return jsonify({
                'id': pedido.id,
                'cliente': pedido.cliente,
                'categoria': pedido.categoria,
                'marca': pedido.marca,
                'producto': pedido.producto,
                'cantidad': pedido.cantidad,
                'precio': pedido.precio
            })
        else:
            return jsonify({'mensaje': 'Pedido no encontrado'}), 404

# Crear un nuevo pedido
@app.route('/pedidos', methods=['POST'])
def create_pedido():
    data = request.get_json()
    cliente = data.get('cliente')
    categoria = data.get('categoria')
    marca = data.get('marca')
    producto = data.get('producto')
    cantidad = data.get('cantidad')
    precio = data.get('precio')

    if not all([cliente, categoria, marca, producto, cantidad, precio]):
        return jsonify({'message': 'Todos los campos son requeridos'}), 400

    new_pedido = Pedido(
        cliente=cliente,
        categoria=categoria,
        marca=marca,
        producto=producto,
        cantidad=cantidad,
        precio=precio
    )
    db.session.add(new_pedido)
    db.session.commit()

    return jsonify({'message': 'Pedido creado exitosamente'}), 201

# Actualizar un pedido existente
@app.route('/pedidos/<int:id>', methods=['PUT'])
def update_pedido(id):
    pedido = Pedido.query.get(id)
    if not pedido:
        return jsonify({'message': 'Pedido no encontrado'}), 404

    data = request.get_json()
    pedido.cliente = data.get('cliente', pedido.cliente)
    pedido.categoria = data.get('categoria', pedido.categoria)
    pedido.marca = data.get('marca', pedido.marca)
    pedido.producto = data.get('producto', pedido.producto)
    pedido.cantidad = data.get('cantidad', pedido.cantidad)
    pedido.precio = data.get('precio', pedido.precio)

    db.session.commit()

    return jsonify({'message': 'Pedido actualizado exitosamente'})

# Eliminar un pedido
@app.route('/pedidos/<int:id>', methods=['DELETE'])
def delete_pedido(id):
    pedido = Pedido.query.get(id)
    if not pedido:
        return jsonify({'message': 'Pedido no encontrado'}), 404

    db.session.delete(pedido)
    db.session.commit()

    return jsonify({'message': 'Pedido eliminado exitosamente'})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
