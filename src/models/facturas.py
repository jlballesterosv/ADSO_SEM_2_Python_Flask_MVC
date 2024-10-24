from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.models import session, Base

class Facturas(Base):
    __tablename__ = "facturas"    
    id = Column(Integer, primary_key=True)
    numero_factura = Column(String(20), unique=True, nullable=False)
    fecha_factura = Column(String(20), nullable=False)
    id_cliente = Column(Integer, ForeignKey('clientes.id'), nullable=False)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'), nullable=False)

    def __init__(self, categoria):
        self.categoria = categoria
    
    def obtener_categorias():
        facturas = session.query(Facturas).all()
        return facturas 
    
    def agregar_factura(factura):
        factura = session.add(factura)
        session.commit()
        return factura