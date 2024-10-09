from flask import Flask, render_template
from src.models import Base, engine
from src.models.productos import Productos

app = Flask(__name__)

app.secret_key = "mi llaveria"
app.debug = True

Base.metadata.create_all(engine)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html', titulo_pagina = 'Inicio')

@app.route('/crear_producto')
def crear_producto():
    return render_template('formulario_crear_producto.html', titulo_pagina = 'Crear Producto')

@app.route('/ver_productos')
def ver_productos():
    productos = Productos.obtener_todos()
    return render_template('tabla_productos.html', titulo_pagina = 'Ver Productos')


    