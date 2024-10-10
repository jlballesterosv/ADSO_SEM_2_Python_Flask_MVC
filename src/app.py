from flask import Flask, render_template, request, redirect, url_for
from src.models import Base, engine
from src.models.productos import Productos
from src.models.categorias import Categorias

app = Flask(__name__)

app.secret_key = "mi llaveria"
app.debug = True

Base.metadata.create_all(engine)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html', titulo_pagina = 'Inicio')

@app.route('/crear_producto', methods=['POST','GET'])
def crear_producto():
    if request.method == 'POST':
        descripcion = request.form.get('descripcion')    
        valor_unitario = request.form.get('valor_unitario')    
        unidad_medida = request.form.get('unidad_medida')    
        cantida_stock = request.form.get('cantida_stock')    
        categoria = request.form.get('categoria')    
        producto = Productos(descripcion,valor_unitario,unidad_medida,cantida_stock,categoria)
        Productos.agregar_producto(producto)
        return redirect(url_for('ver_productos'))
    return render_template('formulario_crear_producto.html', titulo_pagina = 'Crear Producto')

@app.route('/ver_productos')
def ver_productos():
    productos = Productos.obtener_productos()
    return render_template('tabla_productos.html', titulo_pagina = 'Ver Productos', productos=productos)


    