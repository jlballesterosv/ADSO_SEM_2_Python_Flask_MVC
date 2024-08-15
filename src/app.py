from flask import Flask, render_template

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crear_producto')
def crear_producto():
    return render_template('formulario_crear_producto.html')

@app.route('/ver_productos')
def ver_productos():
    return render_template('tabla_productos.html')