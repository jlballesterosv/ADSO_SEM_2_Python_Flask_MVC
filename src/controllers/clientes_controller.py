from src.app import app
from flask import render_template, request, redirect, url_for
from flask_controller import FlaskController
from src.models.clientes import Clientes

class ClientesController(FlaskController):
   
    @app.route('/consultar_cliente_numero_identificacion/<numero_identificacion>')
    def consultar_cliente_numero_identificacion(numero_identificacion):
        cliente = Clientes.obtener_cliente_por_numero_identificacion(numero_identificacion)
        return cliente


        

