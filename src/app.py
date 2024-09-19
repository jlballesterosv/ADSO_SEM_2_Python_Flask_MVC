from flask import Flask, render_template

app = Flask(__name__)

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
    return render_template('tabla_productos.html', titulo_pagina = 'Ver Productos')

class Productos:
    descripcion = 'Carne'
    valor_unitario = 1000
    cantidad_stock = 10
    unidad_medida = 'GRS'
    
    def crear_producto(descripcion, valor_unitario, cantidad_stock, unidad_medida):
        return 'Producto creado correctamente'
    