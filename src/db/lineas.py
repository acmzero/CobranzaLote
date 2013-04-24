'''
Created on Apr 23, 2013

@author: pit
'''
from basededatos import *
from sqlalchemy.schema import Column
from productos import *
from sqlalchemy.orm import backref
from sqlalchemy.types import Float

class Lineas(Base):
    __tablename__ = "lineas"
    linea_id= Column(Integer, primary_key=True)
    linea=Column(Integer)
    cantidad=Column(Integer)
    precio=Column(Float)
    total=Column(Float)
    producto_id=relationship("Producto", backref=backref("producto"))
    