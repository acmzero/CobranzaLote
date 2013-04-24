'''
Created on Apr 23, 2013

@author: pit
'''
from basededatos import *
from sqlalchemy.schema import Column
from clientes import *
from sqlalchemy.orm import backref
from sqlalchemy.types import Date

class Ventas(Base):
    __tablename__ = "ventas"
    venta_id= Column(Integer, primary_key=True)
    fecha=Column(Date)
    folio=Column(String)
    cliente_id=relationship("Clientes", backref=backref("cliente"))
    