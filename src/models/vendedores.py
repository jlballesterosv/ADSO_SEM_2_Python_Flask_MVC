from sqlalchemy import Column, Integer, String, ForeignKey
from src.models import session, Base

class Vendedores(Base):
    __tablename__ = "vendedores"    
    id = Column(Integer, primary_key=True)
    nombre_completo = Column(String(200), nullable=False)
    email = Column(String(500), unique=True, nullable=False)    
    id_usuario = Column(Integer, ForeignKey('usuarios.id'), nullable=False)



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
