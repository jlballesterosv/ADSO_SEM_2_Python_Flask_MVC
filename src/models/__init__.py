from flask_sqlalchemy import SQLAlchemy
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine("mysql+pymysql://root@localhost/factura003?charset=utf8mb4")

connection = engine.connect()

Base = declarative_base()
Base.metadata.bind = engine

Session = sessionmaker(bind=engine)

session = Session()

