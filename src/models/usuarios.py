from sqlalchemy import Column, Integer, String
from src.models import session, Base
from flask_login import UserMixin

class Usuarios(Base, UserMixin):
    __tablename__ = "usuarios"    
    id = Column(Integer, primary_key=True)
    nombre_completo = Column(String(200), nullable=False)
    email = Column(String(500), unique=True, nullable=False)
    contrasena = Column(String(30), nullable=False)
    rol = Column(String(20), nullable=False)


    def __init__(self, 
                 numero_identificacion, 
                 nombre_completo, 
                 direccion, telefono, 
                 email):
        self.numero_identificacion = numero_identificacion
        self.nombre_completo = nombre_completo
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
    
    def obtener_usuarios():
        clientes = session.query(Usuarios).all()
        return clientes 
    
    def validar_usuario(email, contrasena):
        usuario_valido = session.query(Usuarios).filter_by(email=email).first()
        if usuario_valido:
            if usuario_valido.contrasena == contrasena:
                return usuario_valido
        return False
        
    def obtener_usuario_por_id(id):
        usuario = session.query(Usuarios).get(id)
        return usuario
