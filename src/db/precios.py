'''
Created on Apr 23, 2013

@author: pit
'''
from basededatos import *
from sqlalchemy.schema import Column
from productos import *
from sqlalchemy.orm import backref
from sqlalchemy.types import Date, Float

class Precios(Base):
    __tablename__ = "precios"
    precio_id= Column(Integer, primary_key=True)
    fecha=Column(Date)
    producto_id=relationship("Productos", backref=backref("producto"))
    precio=Column(Float)